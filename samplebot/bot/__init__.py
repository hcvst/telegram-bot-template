from telegram.ext import PicklePersistence, Updater

import samplebot.bot.handlers
import samplebot.config


def run():
    updater = Updater(
        samplebot.config.TELEGRAM_TOKEN,
        persistence=PicklePersistence(samplebot.config.PERSISTENCE_FILE),
        use_context=True
    )

    updater.dispatcher.add_handler(samplebot.bot.handlers.conversation_handler)
    updater.dispatcher.add_handler(samplebot.bot.handlers.fallback_handler)
    updater.dispatcher.add_error_handler(samplebot.bot.handlers.error)
    updater.start_polling()
    updater.idle()
