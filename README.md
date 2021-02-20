# image-splitter

**splits an image into RGBA channels**

## Features

* Gives you image format/extension
* Gives you image dimensions
* Gives you number of channels in an image
* Shows you all the image channels i.e. RGB, Grayscale, RGBA
* Splits and saves all the image channels in the current working directory

## How to use ImageSplitter Class?

Following is a demo code, also available in main.py file uploaded in the repo.

```
try:
    from ImageSplitter import ImageSplitter
except ImportError:
    raise ImportError("Couldn't Import ImageSpliiter class")

import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Input an image file to split into channels')
    parser.add_argument('-i', '--input', type=str, required=True, help="Image Path")

    args = vars(parser.parse_args())

    filename = args['input']

    if not filename or len(filename) < 5:
        raise Exception('Please provide an image file path')

    _image = ImageSplitter(filename)
    
    print(_image.image_format)
    print(_image.number_of_channels)
    print(_image.image_dimensions)
    _image.show_channels()
    _image.save_channels()
```

### Improvements are welcome. Thank You :)
