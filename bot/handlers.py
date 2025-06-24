from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

WEBAPP_URL = "https://flip-production-fbfb.up.railway.app"
  # заменишь на свой URL

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


async def webapp_data(message: Message):
    await message.answer(f"📦 Получено из WebApp: {message.web_app_data.data}")

def register_handlers(dp: Dispatcher):
    dp.message.register(start, Command("start"))
    dp.message.register(webapp_data, lambda m: m.web_app_data is not None)
