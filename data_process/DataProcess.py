import os
import re
import pymongo
from data_process.DataExtraction import PreProcess
from data_process.MainData import MainData

class DataProcess():

    def __init__(self, root_path, db):
        self.download_path = os.path.join(root_path, 'downloads')
        self.prefix = ''
        self.rename_dict = {
            'block.csv': 'Block.csv',
            'ShortSelling.csv': 'Short.csv'
        }
        self.db = db

    def process_files(self):
        preProcess = PreProcess(self.download_path)
        preProcess.extract_zip_files()
        self.prefix = preProcess.get_prefix()
        files = os.listdir(self.download_path)
        for f in files:
            if re.search('^cm.*bhav[.]csv$', f):
                preProcess.rename_file(f, 'Main.csv')
            else:
                preProcess.rename_file(f, self.rename_dict[f])

    def process_data(self):
        main_file_data = MainData(self.download_path, self.prefix+'Main.csv', self.db)
        main_file_data.parse_data()