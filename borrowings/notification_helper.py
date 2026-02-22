import requests
from django.conf import settings


def send_telegram_notification(message):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    data = {"chat_id": chat_id, "text": message}

    try:
        response = requests.post(url, data=data, timeout=5)
        response.raise_for_status()
    except Exception as e:
        print(f"Error sending telegram notification: {e}")
