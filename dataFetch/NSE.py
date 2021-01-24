class NSE():

  # initialize class with driver
  def __init__(self, webdriver):
    self.driver = webdriver

  # get the title of the page
  def load_page(self):
    link = "https://www.nseindia.com/"
    self.driver.get(link)

  # close the driver
  def close_page(self):
    self.driver.close()