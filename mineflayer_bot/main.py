```python
import mineflayer
from mineflayer_bot import config, bot, navigation, inventory, combat, mining, building, farming, trading, chat, utils
from mineflayer_bot.tests import test_navigation, test_inventory, test_combat, test_mining, test_building, test_farming, test_trading, test_chat, test_utils

def main():
    # Create a new bot instance
    bot_instance = bot.Bot(config.SERVER, config.USERNAME, config.PASSWORD)

    # Register event handlers
    bot_instance.on('spawn', navigation.navigate)
    bot_instance.on('death', utils.log)
    bot_instance.on('chat', chat.handle_chat)
    bot_instance.on('move', navigation.navigate)
    bot_instance.on('dig', mining.mine)
    bot_instance.on('build', building.build)
    bot_instance.on('trade', trading.trade)
    bot_instance.on('farm', farming.farm)

    # Run tests
    test_navigation.run_tests()
    test_inventory.run_tests()
    test_combat.run_tests()
    test_mining.run_tests()
    test_building.run_tests()
    test_farming.run_tests()
    test_trading.run_tests()
    test_chat.run_tests()
    test_utils.run_tests()

if __name__ == "__main__":
    main()
```