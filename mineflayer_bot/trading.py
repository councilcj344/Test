```python
import mineflayer
from .config import server, username, password
from .bot import bot
from .navigation import navigate
from .inventory import manageInventory
from .utils import log, handleError

def trade():
    try:
        villager = bot.nearestEntity((entity) => entity.type === 'mob' and entity.mobType === 'Villager')
        if villager is None:
            log('No nearby villagers found for trading.')
            return

        navigate(villager.position)

        if not manageInventory('Emerald'):
            log('No emeralds found in inventory for trading.')
            return

        bot.trade(villager, 'Emerald', 1, (err) => {
            if err:
                handleError(err)
            else:
                log('Trade successful.')
        })
    except Exception as e:
        handleError(e)

bot.on('chat', (username, message) => {
    if username === bot.username:
        return

    if message.lower() === 'trade':
        trade()
})
```