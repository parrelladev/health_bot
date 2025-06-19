from telegram import Update
from telegram.ext import ContextTypes

from services.llm_service import LLMService

user_data = {}
llm_service = LLMService()

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    text = update.message.text
    info = user_data.setdefault(user_id, {})

    if 'theme' not in info:
        info['theme'] = text
        await update.message.reply_text("Legal! Agora me diga: quem é o público-alvo desse vídeo?")
    elif 'audience' not in info:
        info['audience'] = text
        prompt = open('prompts/diretrizes_medicas.txt').read() + f"\nTema: {info['theme']}\nPúblico: {info['audience']}"
        script = llm_service.generate_script(prompt)
        info['script'] = script
        await update.message.reply_text(f"Aqui está o roteiro:\n\n{script}\n\nEnvie /aprovar para continuar ou escreva novo texto para ajustar.")
    else:
        # replace script with user provided text
        info['script'] = text
        await update.message.reply_text("Roteiro atualizado. Envie /aprovar para continuar.")
