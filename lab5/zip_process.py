from zip_processor import ZipProcessor
import sys
import os
from PIL import Image


class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string
        
    def process_files(self):
        '''
        Perform a search and replace on all files in the temporary directory
        '''
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open('w') as file:
                file.write(contents)

class ScaleZip(ZipProcessor):
    '''
    Scale each image in the diretory to 640x480
    '''
    for filename in self.temp_directory.iterdir():
        im = Image.open(str(filename))
        scaled = im.resize((640,480))
        scaled.save(str(filename))
        
        