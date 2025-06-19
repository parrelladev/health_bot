from telegram import Update
from telegram.ext import ContextTypes

user_data = {}

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    user_data[user_id] = {'photo': update.message.photo[-1].file_id}
    await update.message.reply_text("Recebi sua foto! Agora, por favor, me envie o tema do vídeo.")
