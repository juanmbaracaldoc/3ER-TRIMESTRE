from django.conf import settings
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = settings.TELEGRAM_BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy un bot hecho con Django.")

def build_app():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    return app
