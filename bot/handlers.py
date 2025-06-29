from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import json
import logging

WEBAPP_URL = "https://flip-production-fbfb.up.railway.app"  # Убедись, что HTTPS!

# Команда /start запускает WebApp
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🚀 Открыть Flipzy", web_app={"url": WEBAPP_URL})]
        ]
    )
    await message.answer(
        "👋 Добро пожаловать в Flipzy!\nНажми кнопку ниже, чтобы открыть мини-приложение.",
        reply_markup=keyboard
    )

# Обработка данных, полученных из MiniApp
async def webapp_data(message: Message):
    try:
        data = json.loads(message.web_app_data.data)
        logging.info(f"📥 WebApp data: {data}")

        # Пример: если получен адрес кошелька
        if data.get("type") == "wallet_connected":
            address = data.get("address")
            await message.answer(f"🔗 Кошелёк подключён: <code>{address}</code>")
        else:
            await message.answer(f"📦 Получено из WebApp: <pre>{json.dumps(data, indent=2)}</pre>")

    except Exception as e:
        logging.exception("Ошибка при обработке данных WebApp")
        await message.answer("⚠️ Не удалось обработать данные из MiniApp.")

# Регистрация обработчиков
def register_handlers(dp: Dispatcher):
    dp.message.register(start, Command("start"))
    dp.message.register(webapp_data, lambda m: m.web_app_data is not None)
