import os
import json
from NSE import NSE
from Driver import Driver

# for additional configuration down the line
config = json.loads(open('./config.json').read())
driver_path = config['root'] + '/chromedriver.exe'

driver = Driver(driver_path)
nse_app = NSE(driver.get_driver())
nse_app.load_page()
nse_app.close_page()
driver.quit()
