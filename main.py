import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from nlp import is_noun_follows_verb
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
    # Get the message text content
    msg_content = update.effective_message.text

    # Ignore messages without text
    if not msg_content:
        return
    
    # Check that the message doesn't have more than 5 words
    if len(msg_content.split()) > 5:
        return

    # Check if a noun immediately follows a verb
    is_follows_verb, verb = is_noun_follows_verb(msg_content)
    if is_follows_verb:
        await update.effective_message.reply_text(f"{verb} deez")

    return


if __name__ == "__main__":
    app = ApplicationBuilder().token(settings.bot_token).build()
    start_handler = CommandHandler("start", start)
    message_handler = MessageHandler(filters.ALL, message_handler)

    app.add_handler(start_handler)
    app.add_handler(message_handler)

    app.run_polling()
