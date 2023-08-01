import unittest
from mineflayer_bot import bot, combat

class TestCombat(unittest.TestCase):
    def setUp(self):
        self.bot = bot.Bot()
        self.combat = combat.Combat(self.bot)

    def test_fight(self):
        self.combat.fight()
        self.assertTrue(self.bot.isFighting)

    def test_stop_fight(self):
        self.combat.stop_fight()
        self.assertFalse(self.bot.isFighting)

    def test_is_enemy_nearby(self):
        self.assertFalse(self.combat.is_enemy_nearby())

if __name__ == '__main__':
    unittest.main()