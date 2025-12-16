from django.core.management.base import BaseCommand
from bot.telegram_bott import build_app  # Asegúrate de que este sea el archivo correcto

class Command(BaseCommand):
    help = "Ejecuta el bot en modo polling"

    def handle(self, *args, **options):
        app = build_app()  # Esto se refiere a la función que creamos en telegram_bott.py
        app.run_polling()
