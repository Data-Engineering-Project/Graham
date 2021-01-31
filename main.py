from data_fetch.DataDownload import DataDownload
from data_process.DataProcess import DataProcess
from config import config
from database import Database

db = Database(config["db"])

if config["data_download"]:
  data_download = DataDownload(config["root_path"])
  data_download.fetch_data()

if config["data_process"]:
  processor = DataProcess(config["root_path"], db)
  processor.process_files()
  processor.process_data()