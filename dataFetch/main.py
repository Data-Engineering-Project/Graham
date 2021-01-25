import os
import json
from NSE import NSE
from Driver import Driver

# for additional configuration down the line
config = json.loads(open('./config.json').read())
root_path = config['root']
driver_path = root_path + '/chromedriver.exe'
download_path = os.path.join(root_path, 'downloads') 

driver = Driver(driver_path, download_path)
nse_app = NSE(driver.get_driver())
nse_app.load_page()
driver.wait_until_downloads_complete()
driver.quit()