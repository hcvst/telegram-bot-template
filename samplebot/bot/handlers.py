import logging
import random
from enum import IntEnum, auto

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler

import samplebot.api
import samplebot.config

logger = logging.getLogger(__name__)


class STATE(IntEnum):
    STARTED = auto()
    END = -1


def start(update, context):
    update.message.reply_text(
        f"Hello {update.message.from_user.first_name} 👋"
    )

    v = context.user_data["visits"] = context.user_data.get("visits", 0) + 1
    if v == 1:
        update.message.reply_photo(
            photo=samplebot.config.WELCOME_PHOTO_URL,
            caption="Welcome!"
        )

    update.message.reply_markdown(
        "How are **you** today?",
        reply_markup=ReplyKeyboardMarkup(
            [
                ["🙂", "🙃"]
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )
    return STATE.STARTED


def respond(update, context):
    resp = "Great" if update.message.text == "🙂" else "¡ʇɐǝɹפ"
    update.message.reply_text(resp)


def fallback(update, context):
    update.message.reply_text(
        "Sorry, I don't know how to help with that. Try /start.",
        reply_markup=ReplyKeyboardRemove()
    )
    return STATE.END


fallback_handler = MessageHandler(Filters.all, fallback)

conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        STATE.STARTED: [
            MessageHandler(Filters.regex(r'🙂|🙃'), respond)
        ]
    },
    fallbacks=[fallback_handler]
)


def error(update, context):
    logger.warning(
        f"Update: {update} - Error: {context.error}"
    )
