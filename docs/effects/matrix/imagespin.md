# Image

**Category:** Matrix

## Settings

### pattern

- Type: `bool`
- Default: `False`
- Description: use a test pattern

### frequency_range

- Type: `In`
- Default: `Lows (beat+bass)`
- Description: Frequency range for the beat detection

### multiplier

- Type: `All`
- Default: `0.5`
- Description: Applied to the audio input to amplify effect

### min_size

- Type: `All`
- Default: `0.3`
- Description: The minimum size multiplier for the image

### bilinear

- Type: `bool`
- Default: `False`
- Description: default NEAREST, use BILINEAR for smoother scaling, expensive on runtime takes a few ms

### spin

- Type: `bool`
- Default: `False`
- Description: spin image according to filter impulse

### clip

- Type: `bool`
- Default: `False`
- Description: When spinning the image, force fit to frame, or allow clipping

### image_source

- Type: `str`
- Description: Load image from

