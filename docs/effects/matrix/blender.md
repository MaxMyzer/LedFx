# Blender

**Category:** Matrix

## Settings

### mask_stretch

- Type: `In`
- Default: `2d full`
- Description: How to stretch the mask source pixles to the effect pixels

### background_stretch

- Type: `In`
- Default: `2d full`
- Description: How to stretch the background source pixles to the effect pixels

### foreground_stretch

- Type: `In`
- Default: `2d full`
- Description: How to stretch the foreground source pixles to the effect pixels

### mask

- Type: `str`
- Description: The virtual from which to source the mask

### foreground

- Type: `str`
- Description: The virtual from which to source the foreground

### background

- Type: `str`
- Description: The virtual from which to source the background

### invert_mask

- Type: `bool`
- Default: `False`
- Description: Switch Foreground and Background

### mask_cutoff

- Type: `All`
- Default: `1.0`
- Description: 1 default = luminance as alpha, anything below 1 is mask cutoff

