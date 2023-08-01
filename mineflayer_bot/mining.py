```python
import mineflayer
from .config import server, username, password
from .bot import bot
from .navigation import navigate
from .inventory import manageInventory

def mine(block):
    if manageInventory('pickaxe'):
        navigate(block.position)
        bot.dig(block)

def find_ores():
    for block in bot.find_blocks():
        if block.name in ['coal_ore', 'iron_ore', 'gold_ore', 'diamond_ore']:
            return block
    return None

def start_mining():
    while True:
        ore = find_ores()
        if ore:
            mine(ore)
        else:
            break

bot.on('spawn', start_mining)
```