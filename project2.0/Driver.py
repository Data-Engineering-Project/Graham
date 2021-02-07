from selenium import webdriver
from kafka import KafkaConsumer, KafkaProducer
import json

class Driver():

  def __init__(self, path_to_driver, download_path):
    # chrome_options = webdriver.ChromeOptions()
    # prefs = {"download.default_directory" : download_path}
    # chrome_options.add_experimental_option("prefs",prefs)
    # self.driver = webdriver.Chrome(executable_path=path_to_driver, chrome_options=chrome_options)
    self.instruction_channel = 'selenium_1'
    self.data_channel = 'data'
    self.instructions = []
    self.consumer = KafkaConsumer(bootstrap_servers="localhost:9092")
    self.consumer.subscribe(self.instruction_channel)
    self.producer = KafkaProducer(bootstrap_servers="localhost:9092")

  def read_instructions(self):
    for msg in self.consumer:
      self.instructions.append(json.loads(msg.value.decode()))

  def goto_page(self, page_link):
    self.driver.get(page_link)

  def _extract_value_by_xpath(self, xpath):
    return self.driver.find_elements_by_xpath(xpath)[0].text

  def extract_values_to_json(self, fields, collection_name):
    collection = {
      "name": collection_name,
      "value": {}
    }
    for field in fields:
      collection["value"][field['key']] = self._extract_value_by_xpath(field['link'])
    return collection

  def exit(self):
    self.driver.close()

  def write_collection_to_db(self, data):
    self.producer.send(self.data_channel, data)


driver = Driver('', '')
driver.read_instructions()
