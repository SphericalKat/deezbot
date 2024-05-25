import logging

from telegram import Update
from telegram.ext import (
    ContextTypes,
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from settings import Settings

settings = Settings()
log_level = logging.getLevelNamesMapping().get(settings.log_level, logging.INFO)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=log_level
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello, deez nuts on yo chin!"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm sorry, I'm a bot and I can't understand that.",
    )


if __name__ == "__main__":
    app = ApplicationBuilder().token(settings.bot_token).build()
    start_handler = CommandHandler("start", start)
    message_handler = MessageHandler(filters.ALL, message_handler)

    app.add_handler(start_handler)
    app.add_handler(message_handler)

    app.run_polling()
