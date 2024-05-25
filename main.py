import logging
import random

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import nlp
from settings import Settings

# Load environment variables
settings = Settings()

# Set the log level
log_level = logging.getLevelNamesMapping().get(settings.log_level, logging.INFO)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=log_level
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello, deez nuts on yo chin!"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    msg_content = msg.text

    if not msg_content:
        return

    # generate exploitable phrases
    exploitable_phrases = nlp.find_exploitable_phrases(msg_content)

    phrase = random.choice(exploitable_phrases)

    await msg.reply_text(f"{phrase} deez")


if __name__ == "__main__":
    app = ApplicationBuilder().token(settings.bot_token).build()
    start_handler = CommandHandler("start", start)
    message_handler = MessageHandler(filters.ALL, message_handler)

    app.add_handler(start_handler)
    app.add_handler(message_handler)

    app.run_polling()
