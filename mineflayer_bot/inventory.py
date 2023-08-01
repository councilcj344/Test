```python
from mineflayer import bot
from mineflayer_bot import config

class InventoryManager:
    def __init__(self, bot):
        self.bot = bot
        self.inventory = bot.inventory

    def get_item_count(self, item_name):
        count = 0
        for item in self.inventory:
            if item.name == item_name:
                count += item.count
        return count

    def has_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return True
        return False

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.bot.use(item)
                return True
        return False

    def drop_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.bot.drop(item)
                return True
        return False

def setup(bot):
    bot.inventory_manager = InventoryManager(bot)
```