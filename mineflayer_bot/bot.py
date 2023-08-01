```python
import mineflayer
from .config import server, username, password
from .navigation import navigate
from .inventory import manageInventory
from .combat import fight
from .mining import mine
from .building import build
from .farming import farm
from .trading import trade
from .chat import chat
from .utils import log, handleError

bot = mineflayer.createBot(server, username, password)

def handleSpawn():
    log("Spawned")
    navigate()

def handleDeath():
    log("Died")
    bot.spawn()

def handleChat(username, message):
    log(f"{username}: {message}")
    chat(message)

def handleMove():
    manageInventory()
    navigate()

def handleDig():
    mine()

def handleBuild():
    build()

def handleTrade():
    trade()

def handleFarm():
    farm()

bot.on('spawn', handleSpawn)
bot.on('death', handleDeath)
bot.on('chat', handleChat)
bot.on('move', handleMove)
bot.on('dig', handleDig)
bot.on('build', handleBuild)
bot.on('trade', handleTrade)
bot.on('farm', handleFarm)

try:
    bot.connect()
except Exception as e:
    handleError(e)
```