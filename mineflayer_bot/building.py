```python
from mineflayer import mineflayer
from .config import server, username, password
from .bot import bot
from .navigation import navigate
from .inventory import manageInventory

class Building:
    def __init__(self):
        self.bot = bot
        self.building_materials = []

    def find_building_materials(self):
        self.building_materials = manageInventory.find_items('building_materials')

    def build(self, blueprint):
        self.find_building_materials()
        if not self.building_materials:
            print("No building materials found in inventory.")
            return
        for step in blueprint:
            x, y, z, block_type = step
            if block_type not in self.building_materials:
                print(f"No {block_type} found in inventory.")
                continue
            navigate.to(x, y, z)
            self.bot.place_block(block_type)

    def repair(self, structure):
        self.find_building_materials()
        if not self.building_materials:
            print("No building materials found in inventory.")
            return
        for block in structure.damaged_blocks:
            x, y, z, block_type = block
            if block_type not in self.building_materials:
                print(f"No {block_type} found in inventory.")
                continue
            navigate.to(x, y, z)
            self.bot.place_block(block_type)

building = Building()
```