import asyncio
import logging
import os
import AIconfig
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from data_processor import get_messages
from ai_logic import prepare_database
from app_core import handle_user

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет")

@dp.message()
async def echo_handler(message: types.Message):
    user_text = message.text
    answer = handle_user(message.from_user.id, user_text)
    await message.answer(answer)

async def main():
    print("Message downloading...")
    history = get_messages(AIconfig.FAQ_FILE)
    print("Database preparing...")
    prepare_database(history)
    print("Bot is started and ready!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")