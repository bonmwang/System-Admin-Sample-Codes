# inventpry_management.py

import json

class Inventory:
  def __init__(self, filename = 'inventory.json'):
    self.filename = filename
    self.load_inventory()


  def load_inventory(self):

    try:

        with open(self.filename, 'r') as file
