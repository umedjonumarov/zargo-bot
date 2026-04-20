import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Токенни текшириб олинг, @BotFather бергани бўлиши керак
TOKEN = "8635095454:AAHXJ080T4_dgmfUCeVxXMDOGOJ4MtcfdUA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    # Бу ерга Render-даги кўк лингингизни қўйинг
    web_url = "https://zargo-bot.onrender.com" 
    
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Do'konni ochish 🛍", web_app=WebAppInfo(url=web_url))]
    ])
    await message.answer("ZarGo дўконига хуш келибсиз!", reply_markup=markup)

async def main():
    print("Бот ишга тушди...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
