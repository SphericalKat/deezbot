import logging

from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler

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


if __name__ == "__main__":
    app = ApplicationBuilder().token(settings.bot_token).build()
    start_handler = CommandHandler("start", start)
    app.add_handler(start_handler)

    app.run_polling()
