import unittest
from mineflayer_bot import bot, farming

class TestFarming(unittest.TestCase):
    def setUp(self):
        self.bot = bot.Bot()
        self.farming = farming.Farming(self.bot)

    def test_start_farming(self):
        self.farming.start_farming()
        self.assertTrue(self.bot.is_farming)

    def test_stop_farming(self):
        self.farming.start_farming()
        self.farming.stop_farming()
        self.assertFalse(self.bot.is_farming)

    def test_farm(self):
        self.farming.farm()
        self.assertTrue(self.bot.is_farming)
        self.assertIsNotNone(self.bot.current_farming_task)

    def test_cancel_farming(self):
        self.farming.farm()
        self.farming.cancel_farming()
        self.assertFalse(self.bot.is_farming)
        self.assertIsNone(self.bot.current_farming_task)

if __name__ == '__main__':
    unittest.main()