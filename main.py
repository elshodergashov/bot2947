from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

import logging
import asyncio


logging.basicConfig(level=logging.INFO)



TOKEN = "8531087320:AAF3YSXo7pzdm-UMfGA0pbVuujcTnSkVjP4"


bot = Bot(token=TOKEN)


dp = Dispatcher()


@dp.message(CommandStart())
async def start_hendler(message: types.Message):
    await message.answer("Salom hammaga")



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())