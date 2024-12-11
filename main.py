import asyncio
import logging
import random

from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from config import token
from image import *
from buttons import *
from inlinekey import *
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
        await message.answer("Your current location🏙?", reply_markup=fire)




    @dp.message(F.text == "Андижан")
    async def russ(message: Message):
        await message.answer_photo(photo="https://media.istockphoto.com/id/2150829608/photo/scenic-view-from-a-quadcopter-of-the-largest-kazakh-city-of-almaty-in-the-early-spring-morning.jpg?s=1024x1024&w=is&k=20&c=DkAZx_h3YVm7sStvEJicTL8CwtedKBIuMWGM2wkMJ2k=", reply_markup=we, caption="добро пожаловать в Андижан"
                                                                                                                                                                                                                                                                                              "\nчто ищете выберете 1 из 4 ")

    @dp.message(F.text == "Andijan")
    async def eng(message: Message):
        await message.answer_photo(photo="https://media.istockphoto.com/id/2150829608/photo/scenic-view-from-a-quadcopter-of-the-largest-kazakh-city-of-almaty-in-the-early-spring-morning.jpg?s=1024x1024&w=is&k=20&c=DkAZx_h3YVm7sStvEJicTL8CwtedKBIuMWGM2wkMJ2k=", reply_markup=g, caption="Welcome to Andijan"
                                                                                                                                                                                                                                                                                               "\nchoose what you need")



@dp.message(F.text == "Кафе")
async def ca(message: Message):
    List = [rasm1, rasm2, rasm3]
    for x in List:
        await message.answer_photo(f"{x}", caption="выберете 1 из 3?", reply_markup=build.as_markup())

@dp.message(F.text == "Cafe")
async def ca(message: Message):
    List = [rasm1, rasm2, rasm3]
    for x in List:
        await message.answer_photo(f"{x}", caption="choose?", reply_markup=build3.as_markup())


    # @dp.message()
    # async def g(message: Message):
    #     text = message.chat
    #     print(text)
    #     if message.text == "да":
    #         await message.reply("ок", reply_markup=gym)
    #     if message.text != "да":
    #         await message.answer("Тогда нажмите кафе еще раз!")







@dp.message(F.text == "Ресторан")
async def res(message: Message):
    a = [rasm4, rasm5, rasm6]
    for x in a:
        await message.answer_photo(f"{x}", caption="🍔:выберете 1 из 3 ресторанов?", reply_markup=build2.as_markup())

@dp.message(F.text == "Restoran")
async def res(message: Message):
    a = [rasm4, rasm5, rasm6]
    for x in a:
        await message.answer_photo(f"{x}", caption="🍔:choose 1 please?", reply_markup=build4.as_markup())

    # @dp.messag    e()
    # async def a(message: Message):
    #     text = message.chat
    #     print(text)
    #     if message.text == "да":
    #         await message.reply("ок", reply_markup=gym)
    #     if message.text != "да":
    #         await message.answer("Тогда нажмите Ресторан еще раз!")



@dp.message(F.text == "Отель")
async def ot(message: Message):
    uy = [rasm7, rasm8, rasm9]
    for x in uy:
        await message.answer_photo(f"{x}", caption="🏝: выберете одну из 3?", reply_markup=ab.as_markup())

@dp.message(F.text == "Hotel")
async def ot(message: Message):
    uy = [rasm7, rasm8, rasm9]
    for x in uy:
        await message.answer_photo(f"{x}", caption="choose 1 hotel?", reply_markup=gf.as_markup())

    # @dp.message()
    # async def a(message: Message):
    #     text = message.chat
    #     print(text)
    #     if message.text == "да":
    #         await message.reply("ок", reply_markup=gym)
    #     if message.text != "да":
    #         await message.answer("Тогда нажмите Отель еще раз!")


@dp.message(F.text == "Парк")
async def ot(message: Message):
    house = [rasm10, rasm11, rasm12]
    for x in house:
        await message.answer_photo(f"{x}", caption="Вам понравилось этот Парк?", reply_markup=ad.as_markup())

@dp.message(F.text == "Park")
async def ot(message: Message):
    house = [rasm10, rasm11, rasm12]
    for x in house:
        await message.answer_photo(f"{x}", caption="choose 1 Park?", reply_markup=gfk.as_markup())

    # @dp.message()
    # async def a(message: Message):
    #     text = message.chat
    #     print(text)
    #     if message.text == "да":
    #         await message.reply("ок", reply_markup=gym)
    #     if message.text != "да":
    #         await message.answer("Тогда нажмите Парк еще раз!")


@dp.message(F.text == "Самарканд")
async def sama(message: Message):
    await message.answer_photo(photo="https://unsplash.com/photos/green-and-brown-concrete-building-x-xwFxX2wVU", reply_markup=we,  caption="добро пожаловать в Самарканд"
                                                                                                                                                "\nчто ищете выберете 1 из 4")

@dp.message(F.text == "Кафе")
async def sama(message: Message):
    f = [rasm13, rasm14, rasm15]
    for x in f:
        await message.answer_photo(f"{x}", caption="Вам понравилось этот Кафе?")

        # @dp.message()
        # async def bm(message: Message):
        #     text = message.chat
        #     print(text)
        #     if message.text == "да":
        #         await message.reply("ок", reply_markup=gym)
        #     if message.text != "да":
        #         await message.reply("Тогда нажмите кафе еще раз!")







async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


