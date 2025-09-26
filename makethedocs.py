
import ast
import os

EFFECTS_DIR = "ledfx/effects"
OUTPUT_PARENT = "docs/effects"


def get_effect_files(effects_dir):
    return [
        os.path.join(effects_dir, f)
        for f in os.listdir(effects_dir)
        if f.endswith(".py") and not f.startswith("__") and os.path.isfile(os.path.join(effects_dir, f))
    ]

def parse_config_schema(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source, filename=file_path)

    name = None
    category = None
    schema_items = []
    # First, find NAME and CATEGORY
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if target.id == "NAME" and isinstance(node.value, ast.Str):
                        name = node.value.s
                    elif target.id == "CATEGORY" and isinstance(node.value, ast.Str):
                        category = node.value.s
    # Now, find CONFIG_SCHEMA assignment
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "CONFIG_SCHEMA":
                    # Expecting vol.Schema({...})
                    if isinstance(node.value, ast.Call) and getattr(node.value.func, 'attr', '') == 'Schema':
                        schema_dict = node.value.args[0] if node.value.args else None
                        if isinstance(schema_dict, ast.Dict):
                            for key, val in zip(schema_dict.keys, schema_dict.values):
                                # key is usually a Call to vol.Optional or vol.Required
                                key_name, desc, default = None, "", ""
                                if isinstance(key, ast.Call) and hasattr(key.func, 'attr'):
                                    if key.args and isinstance(key.args[0], ast.Str):
                                        key_name = key.args[0].s
                                    for kw in key.keywords:
                                        if kw.arg == "description" and isinstance(kw.value, ast.Str):
                                            desc = kw.value.s
                                        if kw.arg == "default" and (isinstance(kw.value, ast.Str) or isinstance(kw.value, ast.Num) or isinstance(kw.value, ast.Constant)):
                                            default = getattr(kw.value, 'value', getattr(kw.value, 'n', getattr(kw.value, 's', "")))
                                elif isinstance(key, ast.Str):
                                    key_name = key.s
                                # Try to get type from val (validator)
                                val_type = ""
                                if isinstance(val, ast.Call) and hasattr(val.func, "attr"):
                                    val_type = val.func.attr
                                elif hasattr(val, "id"):
                                    val_type = val.id
                                schema_items.append({
                                    "name": key_name,
                                    "type": val_type,
                                    "default": default,
                                    "description": desc
                                })
    return name, category, schema_items

def generate_markdown(name, category, schema_items, effect_name):
    md = f"# {name or effect_name}\n\n"
    if category:
        md += f"**Category:** {category}\n\n"
    md += "## Settings\n\n"
    if schema_items:
        for setting in schema_items:
            md += f"### {setting['name']}\n\n"
            if setting["type"]:
                md += f"- Type: `{setting['type']}`\n"
            if setting["default"] != "":
                md += f"- Default: `{setting['default']}`\n"
            if setting["description"]:
                md += f"- Description: {setting['description']}\n"
            md += "\n"
    else:
        md += "_No settings defined._\n"
    return md

def main():
    effect_files = get_effect_files(EFFECTS_DIR)
    for file_path in effect_files:
        name, category, schema_items = parse_config_schema(file_path)
        effect_name = os.path.splitext(os.path.basename(file_path))[0]
        category_dir = os.path.join(OUTPUT_PARENT, (category or "uncategorized").lower())
        os.makedirs(category_dir, exist_ok=True)
        output_file = os.path.join(category_dir, f"{effect_name.lower()}.md")
        if os.path.exists(output_file):
            print(f"Skipping (already exists): {output_file}")
            continue
        md_content = generate_markdown(name, category, schema_items, effect_name)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Generated: {output_file}")

if __name__ == "__main__":
    main()