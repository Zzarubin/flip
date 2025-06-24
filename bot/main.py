import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from bot.handlers import register_handlers
import os
import uvicorn
from webapp_server import app as web_app
import os
print("TOKEN?", os.getenv("TELEGRAM_BOT_TOKEN"))  # для лога

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def main():
    from aiogram.client.default import DefaultBotProperties

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

    dp = Dispatcher(storage=MemoryStorage())
    register_handlers(dp)

    async def start_bot():
        await dp.start_polling(bot)

    async def start_web():
        config = uvicorn.Config(web_app, host="0.0.0.0", port=8000, log_level="info")
        server = uvicorn.Server(config)
        await server.serve()

    await asyncio.gather(start_bot(), start_web())

if __name__ == "__main__":
    asyncio.run(main())
