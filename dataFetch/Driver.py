from selenium import webdriver

class Driver():

  # load the driver and start
  def __init__(self, path_to_driver):
    self.driver = webdriver.Chrome(executable_path=path_to_driver)

  def get_driver(self):
    return self.driver

  # quit the application
  def quit(self):
    self.driver.quit()