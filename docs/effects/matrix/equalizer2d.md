# Equalizer2d

**Category:** Matrix

## Settings

### peak_percent

- Type: `All`
- Default: `1.0`
- Description: Size of the tracer bar that follows a filtered value

### peak_decay

- Type: `All`
- Default: `0.03`
- Description: Decay filter applied to the peak value

### peak_marks

- Type: `bool`
- Default: `False`
- Description: Turn on white peak markers that follow a freq value filtered with decay

### peak_color

- Type: `validate_color`
- Default: `#FFFFFF`
- Description: Peak mark color

### center

- Type: `bool`
- Default: `False`
- Description: Center the equalizer bar

### max_vs_mean

- Type: `bool`
- Default: `False`
- Description: Use max or mean value for bar size

### ring

- Type: `bool`
- Default: `False`
- Description: Why be so square?

### spin

- Type: `bool`
- Default: `False`
- Description: Weeeeeeeeeee

### bands

- Type: `All`
- Default: `16`
- Description: Number of freq bands

### frequency_range

- Type: `In`
- Default: `Lows (beat+bass)`
- Description: Frequency range for spin impulse

### spin_multiplier

- Type: `All`
- Default: `1.0`
- Description: Spin impulse multiplier

### spin_decay

- Type: `All`
- Default: `0.1`
- Description: Decay filter applied to the spin impulse

