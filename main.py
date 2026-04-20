import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Ўзингнинг маълумотларингни шу ерга ёз:
TOKEN = "8635095454:AAHXJ080T4_dgmfUCeVxXMDOGOJ4MtcfdUA"  # BotFather берган токен
ADMIN_ID = 888856976          # Сенинг Telegram ID рақаминг

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    # Диққат: index.html файлинг қаердалигини кўрсатамиз
    # Ҳозирча тест учун оддий тугма қиламиз
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Do'konni ochish 🛍", web_app=WebAppInfo(url="https://zargo-bot.onrender.com"))] 
    ])
    await message.answer("ZarGo дўконига хуш келибсиз!", reply_markup=markup)

async def main():
    print("Бот ишга тушди...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
