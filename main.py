import asyncio
import logging
import random

from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from config import token
from image import *
from buttons import *
from aiogram import Dispatcher, F, Bot

TOKEN = token

router = Router()
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Hello {message.from_user.first_name}👋, choose your language.\n"
                         f"Здраствуйте {message.from_user.first_name}👋, выберете язык чтобы продолжить.\n", reply_markup=keyboard)


    @dp.message(F.text == "Russian")
    async def russ(message: Message):
        await message.answer("на данный момент ваше местоположение🏙?", reply_markup=f)

    @dp.message(F.text == "English")
    async def eng(message: Message):
        await message.answer("Your current location🏙?", reply_markup=f)



    @dp.message(F.text == "Andijon")
    async def russ(message: Message):
        await message.answer_photo(photo="https://media.istockphoto.com/id/2150829608/photo/scenic-view-from-a-quadcopter-of-the-largest-kazakh-city-of-almaty-in-the-early-spring-morning.jpg?s=1024x1024&w=is&k=20&c=DkAZx_h3YVm7sStvEJicTL8CwtedKBIuMWGM2wkMJ2k=", reply_markup=g, caption="добро пожаловать а Андижан"
                                                                                                                                                                                                                                                                                              "\nчто ищете выберете 1 из 4 ")



@dp.message(F.text == "Cafe")
async def cafe(message: Message):
    List = [rasm1, rasm2, rasm3]
    away = random.choice(List)
    await message.answer_photo(f"{away}", reply_markup=golf, caption="Sizga bu cafe yoqdimi?")   # noqa


@dp.message(F.text == "Back")
async def back(message: Message):
    await message.answer("", reply_markup=g)

# @dp.message(F.text == "Contact")
# async def con(message: Message):
#     f = message.from_user.first_name
#     await message.answer_contact("+ 74 226 66 63", first_name=f)


# @dp.message(F.text == "Cafe")
# async def cafe(message: Message):
#     f = message.from_user.first_name
#     await message.answer_contact("+909187086", first_name=f, reply_markup=golf)










async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

