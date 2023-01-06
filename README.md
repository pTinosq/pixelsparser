# pixelsparser

A python library that allows users to import their Pixels JSON data and use it in their python scripts.

## Installation

Install the library using pip:

```bash
pip install pixelsparser
```

## Usage

```python
import pixelsparser

pixels = pixelsparser.load("location/to/data.json")

# Access the mood of the first pixel
print(pixels[0].mood)

# Access the notes of the second pixel
print(pixels[1].notes)
```

## Credits

This library was created to parse data from the Pixels app by Teo Vogel, available on the [Google Play Store](https://play.google.com/store/apps/details?id=ar.teovogel.yip) and on the [App Store](https://apps.apple.com/sg/app/pixels-mental-health-and-mood/id1481910141)
