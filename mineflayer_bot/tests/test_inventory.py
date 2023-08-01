import unittest
from mineflayer_bot import bot, inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.bot = bot.Bot()
        self.inventory = inventory.Inventory(self.bot)

    def test_add_item(self):
        self.inventory.add_item('diamond', 5)
        self.assertEqual(self.inventory.get_item_count('diamond'), 5)

    def test_remove_item(self):
        self.inventory.add_item('diamond', 5)
        self.inventory.remove_item('diamond', 2)
        self.assertEqual(self.inventory.get_item_count('diamond'), 3)

    def test_get_item_count(self):
        self.inventory.add_item('diamond', 5)
        self.assertEqual(self.inventory.get_item_count('diamond'), 5)

    def test_clear_inventory(self):
        self.inventory.add_item('diamond', 5)
        self.inventory.clear_inventory()
        self.assertEqual(self.inventory.get_item_count('diamond'), 0)

if __name__ == '__main__':
    unittest.main()