'''
Image Splitter -> Split any image into multiple channels.
RGBA image would be splitted into 4 channels.
RGB would be splitted into 3 channels only.
'''

import os, sys

try:
    from PIL import Image
except ImportError:
    raise ImportError("Couldn't find Pillow module. use >pip install pillow")

__author__  = 'mujeebishaque'
__version__ = 'v1.0'


class ImageSplitter:
    
    image_file      = None
    image_file_path = None

    def __init__(self, file_path):
        if os.path.exists(str(file_path)) or os.path.isfile(str(file_path)):
            self.image_file   = Image.open(str(file_path))
        else:
            raise FileExistsError("Couldn't find file. Please provide a valid file path.")

    @property
    def number_of_channels(self):
        return self.image_file.getbands().__len__()
    
    @property
    def image_format(self):
        return self.image_file.format.__str__()

    @property
    def image_dimensions(self):
        return self.image_file.size.__str__()
        
    def show_channels(self):
        # show channels imshow simultaneously
        if self.number_of_channels == 1:
            self.image_file.show()            
        
        if self.number_of_channels == 3:
            r, g, b = self.image_file.split()
            r.show()
            g.show()
            b.show()
        
        if self.number_of_channels == 4:
            r, g, b, a = self.image_file.split()
            r.show()
            g.show()
            b.show()
            a.show()
        
    def save_channels(self):
        # Save image channels in current working directory
        if self.number_of_channels == 1:
            sys.stdout.writelines(''' 
            -------------------------------------
                THIS IMAGE HAS ALREADY ONE CHANNEL ONLY. NO NEED TO PROCEED.
            -------------------------------------
            ''')
            return
        
        if self.number_of_channels == 3:
            r, g, b = self.image_file.split()
            r.save()
            g.save()
            b.save()
        
        if self.number_of_channels == 4:
            r, g, b, a = self.image_file.split()
            r.save()
            g.save()
            b.save()
            a.save()