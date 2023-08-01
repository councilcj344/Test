```python
import mineflayer
from .config import BOT_USERNAME, BOT_PASSWORD, SERVER_IP, SERVER_PORT
from .bot import bot
from .navigation import navigate_to
from .inventory import manage_inventory

def fight(target):
    bot.attack(target, True)

def on_entity_spawned(entity):
    if entity.type == 'mob' and entity.mobType == 'Zombie':
        navigate_to(entity.position)
        manage_inventory('Sword')
        fight(entity)

def on_entity_moved(entity):
    if entity.type == 'mob' and entity.mobType == 'Zombie':
        navigate_to(entity.position)
        manage_inventory('Sword')
        fight(entity)

def on_death():
    print(f"{BOT_USERNAME} died...")

bot.on('entitySpawn', on_entity_spawned)
bot.on('entityMoved', on_entity_moved)
bot.on('death', on_death)

if __name__ == "__main__":
    bot.connect(SERVER_IP, SERVER_PORT, BOT_USERNAME, BOT_PASSWORD)
```