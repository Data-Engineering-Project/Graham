import json
from data_fetch.DataDownload import DataDownload
from data_process.DataProcess import DataProcess

config = json.loads(open('./config.json').read())
root_path = config['root']

try:
  delete_files_after_processing = config['delete_files_after_processing']
except:
  delete_files_after_processing = True

data_download = DataDownload(root_path)
data_download.fetch_data()

processor = DataProcess(root_path)
processor.process_data()
