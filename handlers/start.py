from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Olá! Sou o bot que vai te ajudar a criar vídeos médicos dentro das normas éticas.\n\nVamos começar? Envie uma foto sua."
    )
