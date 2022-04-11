from typing import Iterable

from scbw.bot_storage import BotStorage
from scbw.player import BotPlayer


def retrieve_bot(
        bot_name: str,
        bot_storages: Iterable[BotStorage]
) -> BotPlayer:
    bot = None
    for bot_storage in bot_storages:
        maybe_bot = bot_storage.find_bot(bot_name)
        if maybe_bot:
            bot = maybe_bot
            break

    if bot is None:
        raise Exception(f"Could not find bot {bot_name}")

    return bot
