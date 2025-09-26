# Keybeat2d

**Category:** Matrix

## Settings

### stretch_horizontal

- Type: `All`
- Default: `100`
- Description: Percentage of original to matrix width

### stretch_vertical

- Type: `All`
- Default: `100`
- Description: Percentage of original to matrix height

### center_horizontal

- Type: `All`
- Default: `0`
- Description: Center offset in horizontal direction percent of matrix width

### center_vertical

- Type: `All`
- Default: `0`
- Description: Center offset in vertical direction percent of matrix height

### image_location

- Type: `str`
- Description: Load gif from url or path

### beat_frames

- Type: `str`
- Description: Frame index to interpolate beats between

### skip_frames

- Type: `str`
- Description: Frames to remove from gif animation

### deep_diag

- Type: `bool`
- Default: `False`
- Description: Diagnostic overlayed on matrix

### fake_beat

- Type: `bool`
- Default: `False`
- Description: Trigger test code with 0.05 beat per frame

### keep_aspect_ratio

- Type: `bool`
- Default: `False`
- Description: Preserve aspect ratio if force fit

### force_fit

- Type: `bool`
- Default: `False`
- Description: Force fit to matrix

### ping_pong_skip

- Type: `bool`
- Default: `False`
- Description: When ping pong, skip the first beat key frame on both ends, use when key beat frames are very close to start and ends only

### ping_pong

- Type: `bool`
- Default: `False`
- Description: Play gif forward and reverse, not just loop

### half_beat

- Type: `bool`
- Default: `False`
- Description: half the beat input impulse, slow things down

### image_brightness

- Type: `All`
- Default: `1.0`
- Description: Image brightness

