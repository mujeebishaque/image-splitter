'''
Image Splitter -> Split any image into multiple channels.
RGBA image would be splitted into 4 channels.
RGB would be splitted into 3 channels only.
'''
import os
try:
    from PIL import Image
except ImportError:
    raise ImportError("Couldn't find Pillow module. use >pip install pillow")

__author__  = 'mujeebishaque'
__version__ = 'v1.0'


class ImageSplitter:
    
    image_file   = None
    image_exists = False

    def __init__(self, file_path):
        if os.path.exists(str(file_path)) or os.path.isfile(str(file_path)):
            self.image_file = Image.open(str(file_path))
        else:
            raise FileExistsError("Couldn't find file. Please provide a valid file path.")

    def determine_format(self):
        img = Image.open(self.image_file)
        image_format = img.format
        return str(image_format)
    
    @property
    def number_of_channels(self):
        return self.image_file.getbands()
    
    @property
    def image_format(self):
        return self.determine_format().__str__()

    def image_channels(self):
        return self.image_file.mode.__str__()

