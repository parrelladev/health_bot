from telegram import Update
from telegram.ext import ContextTypes

from services.heygen_service import HeyGenService
from handlers.briefing import user_data

heygen_service = HeyGenService()

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    info = user_data.get(user_id)
    if not info or 'photo' not in info or 'script' not in info:
        await update.message.reply_text('Informações incompletas. Envie uma foto e o briefing.')
        return
    video_url = heygen_service.generate_video(info['photo'], info['script'])
    await update.message.reply_text(f'Vídeo gerado: {video_url}')
