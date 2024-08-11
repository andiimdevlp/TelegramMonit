from telethon import TelegramClient
from bot.config import api_id, api_hash, phone_number
from bot.logger import initialize_log
from bot.handlers import register_handlers

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone=phone_number)
    initialize_log()
    register_handlers(client)
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
