import json
import os
import zipfile
import re

class PreProcess():
  
  def __init__(self, download_path):
    self.downlad_folder = download_path

  def extract_zip_files(self):
    for f in os.listdir(self.downlad_folder):
      extension = os.path.splitext(f)[1]
      if extension == '.zip':
        with zipfile.ZipFile(os.path.join(self.downlad_folder, f), 'r') as zip_ref:
          zip_ref.extractall(self.downlad_folder)
        os.remove(os.path.join(self.downlad_folder,f))

  def rename_files(self, new_filename = ''):
    files = os.listdir(self.downlad_folder)
    new_filename = ''
    for f in files:
      if re.search('^cm.*bhav[.]csv$', f):
        new_filename = re.search('^cm(.*)bhav[.]csv$', f).group(1)
        os.rename(os.path.join(self.downlad_folder, f), os.path.join(self.downlad_folder, new_filename + 'Main.csv'))
    rename_dict = {
      'block.csv': new_filename + 'Block.csv',
      'ShortSelling.csv':new_filename + 'Short.csv'
    }
    for f in files:
      if f in rename_dict:
        src = os.path.join(self.downlad_folder, f)
        dst = os.path.join(self.downlad_folder, rename_dict[f])
        os.rename(src, dst)
 