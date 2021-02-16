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
            self.image_file   = Image.open(str(file_path))
            self.image_exists = True
        else:
            raise FileExistsError("Couldn't find file. Please provide a valid file path.")

    @property
    def number_of_channels(self):
        return len(self.image_file.mode.__str__())
    
    @property
    def image_format(self):
        return self.image_file.format.__str__()

    def image_channels(self):
        data   = self.image_file.getdata()
        r = [(d[0], 0, 0) for d in data]
        g = [(0, d[1], 0) for d in data]
        b = [(0, 0, d[2]) for d in data]
        
    def show_channels(self):
        # show channels imshow simultaneously
        r, g, b = self.image_file.split()

    def save_channels(self):
        data = self.image_file.getdata()
        # Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
        r = [(d[0], 0, 0) for d in data]
        g = [(0, d[1], 0) for d in data]
        b = [(0, 0, d[2]) for d in data]

        img.putdata(r)
        img.save('r.png')
        img.putdata(g)
        img.save('g.png')
        img.putdata(b)
        img.save('b.png')