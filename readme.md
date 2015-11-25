# Repository for _Car Plates Reader_

The scripts contained herein are meant to process the videos and images from public cameras (or
cameras in public transport) to find A-lane or other statically identifiable violators.

## Helpers

### Converting video stream to PNG images

```bash
ffmpeg -i /path/to/video.avi -vf fps=1 out/%d.png
```

