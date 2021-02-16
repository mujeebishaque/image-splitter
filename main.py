try:
    from ImageSplitter import ImageSplitter
except ImportError:
    raise ImportError("Couldn't Import ImageSpliiter class")

import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Input an image file', epilog="Star us on Github")
    parser.add_argument('-i', '--input', type=str, required=True, help="Image Path")

    args = vars(parser.parse_args())

    filename = args['input']

    if not filename or len(filename) < 5:
        raise Exception('Please provide an image file path')

    _image = ImageSplitter(filename)
    print(_image.image_format)
    print(_image.number_of_channels)
    print(_image.image_dimensions)