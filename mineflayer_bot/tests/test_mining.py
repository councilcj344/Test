import unittest
from mineflayer_bot import mining, bot

class TestMining(unittest.TestCase):

    def setUp(self):
        self.bot = bot.Bot()
        self.mining = mining.Mining(self.bot)

    def test_mine_block(self):
        block = self.bot.find_nearest_block('stone')
        self.assertIsNotNone(block, "No stone block found")
        self.mining.mine_block(block)
        self.assertFalse(self.bot.is_block_present(block), "Block not mined")

    def test_mine_ore(self):
        ore = self.bot.find_nearest_block('iron_ore')
        self.assertIsNotNone(ore, "No iron ore found")
        self.mining.mine_block(ore)
        self.assertFalse(self.bot.is_block_present(ore), "Ore not mined")

    def test_mine_multiple_blocks(self):
        blocks = self.bot.find_blocks('stone', 10)
        self.assertGreaterEqual(len(blocks), 10, "Not enough stone blocks found")
        self.mining.mine_blocks(blocks)
        for block in blocks:
            self.assertFalse(self.bot.is_block_present(block), "Block not mined")

if __name__ == '__main__':
    unittest.main()