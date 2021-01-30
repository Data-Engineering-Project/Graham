import os
import pandas as pd

class MainData():

  def __init__(self, download_folder, file_name, db):
    self.file = os.path.join(download_folder, file_name)
    self.db = db
    pass

  def parse_data(self):
    data = pd.read_csv(self.file)
    # del data[12]
    print(data)
    