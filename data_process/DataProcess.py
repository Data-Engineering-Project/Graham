import os
from data_process.DataExtraction import PreProcess

class DataProcess():

    def __init__(self, root_path):
        self.download_path = os.path.join(root_path, 'downloads')

    def process_data(self):
        preProcess = PreProcess(self.download_path)
        preProcess.extract_zip_files()
        preProcess.rename_files()
        