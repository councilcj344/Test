import unittest
from mineflayer_bot import trading

class TestTrading(unittest.TestCase):

    def setUp(self):
        self.bot = trading.Bot()

    def test_trade(self):
        self.bot.trade('diamond')
        self.assertIn('diamond', self.bot.inventory)

    def test_trade_failure(self):
        with self.assertRaises(trading.TradeException):
            self.bot.trade('nonexistent_item')

    def test_trade_success(self):
        self.bot.trade('iron')
        self.assertIn('iron', self.bot.inventory)

    def test_trade_with_villager(self):
        self.bot.trade_with_villager('farmer', 'wheat')
        self.assertIn('emerald', self.bot.inventory)

    def test_trade_with_villager_failure(self):
        with self.assertRaises(trading.TradeException):
            self.bot.trade_with_villager('farmer', 'nonexistent_item')

    def test_trade_with_villager_success(self):
        self.bot.trade_with_villager('farmer', 'potato')
        self.assertIn('emerald', self.bot.inventory)

if __name__ == '__main__':
    unittest.main()