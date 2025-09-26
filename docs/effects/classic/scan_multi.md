# Scan Multi

**Category:** Classic

## Settings

### blur

- Type: `All`
- Default: `3.0`
- Description: Amount to blur the effect

### mirror

- Type: `bool`
- Default: `False`
- Description: Mirror the effect

### bounce

- Type: `bool`
- Default: `True`
- Description: bounce the scan

### scan_width

- Type: `All`
- Default: `30`
- Description: Width of scan eye in %

### speed

- Type: `All`
- Default: `50`
- Description: Scan base % per second

### color_low

- Type: `validate_color`
- Default: `#FF0000`
- Description: Color of low power scan

### color_mid

- Type: `validate_color`
- Default: `#00FF00`
- Description: Color of mid power scan

### color_high

- Type: `validate_color`
- Default: `#0000FF`
- Description: Color of high power scan

### multiplier

- Type: `All`
- Default: `3.0`
- Description: Speed impact multiplier

### color_intensity

- Type: `bool`
- Default: `True`
- Description: Adjust color intensity based on audio power

### use_grad

- Type: `bool`
- Default: `False`
- Description: Use colors from gradient selector

### input_source

- Type: `In`
- Default: `Power`
- Description: Audio processing source for low, mid, high

### attack

- Type: `All`
- Default: `0.9`
- Description: Filter damping on attack, lower number is more

### decay

- Type: `All`
- Default: `0.7`
- Description: Filter damping on decay, lower number is more

### filter

- Type: `bool`
- Default: `False`
- Description: Enable damping filters on attack and decay

