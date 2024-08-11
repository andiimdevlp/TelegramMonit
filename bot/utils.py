import os

async def download_media(event):
    try:
        return await event.message.download_media()
    except Exception as e:
        print(f"Erro ao baixar mídia: {e}")
        return None

def remove_media_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Erro ao remover arquivo: {e}")

def extract_media_info(media):
    return {
        "document_id": media.document.id if hasattr(media, 'document') else None,
        "size": media.document.size if hasattr(media, 'document') else None,
        "mime_type": media.document.mime_type if hasattr(media, 'document') else None
    } if media else None
