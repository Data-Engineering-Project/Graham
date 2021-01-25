class NSE():

  # initialize class with driver
  def __init__(self, webdriver):
    self.driver = webdriver

  # get the title of the page
  def load_page(self):
    link = "https://www1.nseindia.com/products/content/all_daily_reports.htm"
    # page_load_delay = 3
    date_xpath = '/html/body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/ul/li[4]/font[1]/b'
    bhavcopy_xpath = '/html/body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/table/tbody/tr[3]/td[1]/a'
    
    self.driver.get(link)
    today_date = self.driver.find_elements_by_xpath(date_xpath)[0].text
    bhavcopy_link = self.driver.find_elements_by_xpath(bhavcopy_xpath)[0]
    print(today_date)
    bhavcopy_link.click()

  # close the driver
  def close_page(self):
    self.driver.close()