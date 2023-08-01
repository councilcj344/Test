import unittest
from mineflayer_bot import bot, building

class TestBuilding(unittest.TestCase):

    def setUp(self):
        self.bot = bot.Bot()
        self.building = building.Building(self.bot)

    def test_build(self):
        self.building.build('wood', (0, 0, 0))
        self.assertTrue(self.bot.world.getBlock((0, 0, 0)).name == 'wood')

    def test_demolish(self):
        self.building.build('wood', (0, 0, 0))
        self.building.demolish((0, 0, 0))
        self.assertTrue(self.bot.world.getBlock((0, 0, 0)).name == 'air')

if __name__ == '__main__':
    unittest.main()