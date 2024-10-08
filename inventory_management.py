# inventory_management.py

"""
This script manages an inventory of hardware and software assets.
It allows adding and removing items and saves the inventory in a JSON file.
"""

import json

class Inventory:
    def __init__(self, filename='inventory.json'):
        self.filename = filename
        self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                self.items = json.load(file)
        except FileNotFoundError:
            self.items = {}

    def save_inventory(self):
        """Save inventory to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.items, file, indent=4)

    def add_item(self, item_name, quantity):
        """Add an item to the inventory."""
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        self.save_inventory()

    def remove_item(self, item_name, quantity):
        """Remove an item from the inventory."""
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:
                del self.items[item_name]
        self.save_inventory()

if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item("Laptop", 5)
    inventory.remove_item("Laptop", 2)
    print(inventory.items)
