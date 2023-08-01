```python
import mineflayer
from mineflayer_bot import config, bot

class Navigation:
    def __init__(self, bot_instance):
        self.bot = bot_instance

    def navigate_to(self, destination):
        path = self.bot.navigate.findPathSync(destination)
        if path.status == 'success':
            self.bot.navigate.walk(path.path)
        else:
            print("No path found!")

    def follow_player(self, player_name):
        player_entity = self.bot.players[player_name].entity
        if player_entity:
            self.bot.navigate.to(player_entity.position)

    def stop_navigation(self):
        self.bot.navigate.stop()

if __name__ == "__main__":
    bot_instance = bot.Bot(config.SERVER, config.USERNAME, config.PASSWORD)
    navigation = Navigation(bot_instance)
    navigation.navigate_to(mineflayer.vec3(100, 64, 0))  # Example destination
```
