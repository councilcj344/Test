import unittest
from mineflayer_bot import bot, chat

class TestChat(unittest.TestCase):

    def setUp(self):
        self.bot = bot.Bot()
        self.chat_module = chat.Chat(self.bot)

    def test_send_message(self):
        self.chat_module.send_message("Hello, world!")
        self.assertEqual(self.bot.last_message, "Hello, world!")

    def test_receive_message(self):
        self.bot.simulate_chat_message("Hello, bot!")
        self.assertEqual(self.chat_module.last_received_message, "Hello, bot!")

    def test_chat_event(self):
        self.bot.simulate_chat_event("Player1", "Hello, bot!")
        self.assertEqual(self.chat_module.last_chat_event, ("Player1", "Hello, bot!"))

if __name__ == '__main__':
    unittest.main()