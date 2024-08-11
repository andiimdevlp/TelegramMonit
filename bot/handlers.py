from telethon import TelegramClient, events
from .logger import log_message, create_log_entry
from .utils import download_media, remove_media_file, extract_media_info
from .config import target_chat_id

async def message_handler(event, client):
    media_info = None
    status = "sucesso"

    try:
        if event.message.media:
            media_info = extract_media_info(event.message.media)
        
        try:
            await client.send_message(target_chat_id, event.message)
        except Exception:
            file_path = await download_media(event)
            if file_path:
                await client.send_file(target_chat_id, file_path, caption=event.message.message)
                remove_media_file(file_path)
            else:
                status = "falha"

    except Exception as e:
        status = "erro"
        print(f"Erro ao processar mensagem: {e}")
    
    log_entry = create_log_entry(event, status, media_info)
    log_message(log_entry)

def register_handlers(client):
    client.on(events.NewMessage)(lambda event: message_handler(event, client))
