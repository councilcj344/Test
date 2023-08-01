```python
from mineflayer_bot import bot
from mineflayer_bot import navigation
from mineflayer_bot import inventory
from mineflayer_bot import utils

class Farming:
    def __init__(self, bot_instance):
        self.bot = bot_instance
        self.navigation = navigation.Navigation(self.bot)
        self.inventory = inventory.Inventory(self.bot)

    def find_farm(self):
        farms = self.bot.find_blocks('wheat')
        if farms:
            return farms[0]
        else:
            return None

    def go_to_farm(self, farm_location):
        self.navigation.navigate_to(farm_location)

    def harvest(self, farm_location):
        self.bot.dig(farm_location)

    def plant(self, farm_location):
        if self.inventory.has_item('wheat_seeds'):
            self.bot.place_block(farm_location, 'wheat_seeds')

    def farm(self):
        farm_location = self.find_farm()
        if farm_location:
            self.go_to_farm(farm_location)
            self.harvest(farm_location)
            self.plant(farm_location)
        else:
            utils.log('No farm found')

def start_farming():
    bot_instance = bot.Bot()
    farming = Farming(bot_instance)
    farming.farm()

if __name__ == "__main__":
    start_farming()
```