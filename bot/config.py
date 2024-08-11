import os

api_id = os.getenv("TELEGRAM_API_ID", "YOUR_API_ID")  # Substitua pelo seu API ID
api_hash = os.getenv("TELEGRAM_API_HASH", "YOUR_API_HASH")  # Substitua pelo seu API Hash
phone_number = os.getenv("TELEGRAM_PHONE_NUMBER", "+5511999999999")  # Substitua pelo seu número de telefone

source_chat_id = int(os.getenv("SOURCE_CHAT_ID", -1001111111111))  # Substitua pelo ID do chat de origem
target_chat_id = int(os.getenv("TARGET_CHAT_ID", -1002222222222))  # Substitua pelo ID do chat de destino
log_file = "telethon_bot_log.json"
