import os
import pandas as pd

class MainData():

  def __init__(self, download_folder, file_name, db):
    self.file = os.path.join(download_folder, file_name)
    self.db = db
    pass

  def parse_data(self):
    data = pd.read_csv(self.file)
    del data[data.keys()[13]]
    data = data[data['SERIES'] == 'EQ']
    save_data = data.to_dict(orient='records')
    print(save_data[1:5])
    self.db.write_many_to_collection('equity', save_data)
    