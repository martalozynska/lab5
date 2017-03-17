import os
import shutil
import zipfile
import time

class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = Path('{}'.format(zipname[:-4]))
    
    def process_zip(self, n=3):
        '''
        Unziping files in n minutes. Default = 3
        '''
        self.unzip_files()
        c = time.time()
        print('Loading...')
        while time.time() - c < n*60:
            pass
        self.zip_files()
        print('Ready!')
    
    def unzip_files(self):
        '''
        Unziping ZipProcessor object
        '''
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.exctracall(str(self.temp_directory))
            
    def zip_files(self):
        '''
        Ziping ZipProcessor object.
        :return:
        '''
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))
