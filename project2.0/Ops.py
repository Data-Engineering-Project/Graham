import os
from os import path
import json
from kafka import KafkaProducer

class Ops():

  def __init__(self):
    self.operations = []
    self.ops_folder_path = path.join(os.getcwd(), "project2.0", "ops")

  def read_all_operations(self):
    for filename in os.listdir(self.ops_folder_path):
      ops_file = path.join(self.ops_folder_path, filename)
      with open(ops_file) as f:
        self.operations.append(f.read())

  def write_operations_to_queue(self, python_selenium_instance, instruction):
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    producer.send(python_selenium_instance, instruction)
    producer.close()

  def distribute_operations(self):
    for operation in self.operations:
      self.write_operations_to_queue("selenium_1", operation.encode())


operations = Ops()
operations.read_all_operations()
operations.distribute_operations()