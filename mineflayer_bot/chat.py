```python
from mineflayer_bot import bot
from mineflayer_bot import config
from mineflayer_bot import utils

class Chat:
    def __init__(self):
        self.bot = bot.Bot()

    def send_message(self, message):
        self.bot.chat(message)

    def handle_chat(self, username, message):
        if username == self.bot.username:
            return

        if 'hello' in message:
            self.send_message('Hello, {}!'.format(username))
        elif 'bye' in message:
            self.send_message('Goodbye, {}!'.format(username))
        else:
            self.send_message('I am a bot. I do not understand your message.')

    def start_listening(self):
        self.bot.on('chat', self.handle_chat)

if __name__ == "__main__":
    chat = Chat()
    chat.start_listening()
```