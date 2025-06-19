import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from handlers.start import start
from handlers.upload import handle_photo
from handlers.briefing import handle_text
from handlers.approval import approve


def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN env var not set")

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("aprovar", approve))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text))

    application.run_polling()


if __name__ == "__main__":
    main()
