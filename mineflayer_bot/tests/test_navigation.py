import unittest
from mineflayer_bot import navigation

class TestNavigation(unittest.TestCase):

    def setUp(self):
        self.bot = navigation.BotNavigation()

    def test_move_to(self):
        self.bot.move_to((10, 10, 10))
        self.assertEqual(self.bot.position, (10, 10, 10))

    def test_move_by(self):
        initial_position = self.bot.position
        self.bot.move_by((5, 5, 5))
        self.assertEqual(self.bot.position, (initial_position[0]+5, initial_position[1]+5, initial_position[2]+5))

    def test_turn_to(self):
        self.bot.turn_to(90)
        self.assertEqual(self.bot.yaw, 90)

    def test_turn_by(self):
        initial_yaw = self.bot.yaw
        self.bot.turn_by(45)
        self.assertEqual(self.bot.yaw, initial_yaw+45)

if __name__ == '__main__':
    unittest.main()