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
        await message.answer_photo(photo="https://media.istockphoto.com/id/2150829608/photo/scenic-view-from-a-quadcopter-of-the-largest-kazakh-city-of-almaty-in-the-early-spring-morning.jpg?s=1024x1024&w=is&k=20&c=DkAZx_h3YVm7sStvEJicTL8CwtedKBIuMWGM2wkMJ2k=", reply_markup=we,  caption="добро пожаловать в Андижан"
                                                                                                                                                                                                                                                                                              "\nчто ищете выберете 1 из 4 ")



@dp.message(F.text == "Кафе")
async def ca(message: Message):
    List = [rasm1, rasm2, rasm3]
    away = random.choice(List)
    await message.answer_photo(f"{away}", caption="Вам понравилось этот Кафе?")

    @dp.message()
    async def g(message: Message):
        text = message.chat
        print(text)
        if message.text == "да":
            await message.reply("ок", reply_markup=gym)
        if message.text != "да":
            await message.answer("Тогда нажмите кафе еще раз!")




@dp.message(F.text == "Ресторан")
async def res(message: Message):
    a = [rasm4, rasm5, rasm6]
    b = random.choice(a)
    await message.answer_photo(f"{b}", caption="🍔:Вам понравилось этот Ресторан?"
                                               "\n✅: если понравился напишите да"
                                               "\n❌: если не понравился напишите нет")

    @dp.message()
    async def a(message: Message):
        text = message.chat
        print(text)
        if message.text == "да":
            await message.reply("ок", reply_markup=gym)
        if message.text != "да":
            await message.answer("Тогда нажмите Ресторан еще раз!")



@dp.message(F.text == "Отель")
async def ot(message: Message):
    uy = [rasm7, rasm8, rasm9]
    l = random.choice(uy)
    await message.answer_photo(f"{l}", caption="Вам понравилось этот Отель?")

    @dp.message()
    async def a(message: Message):
        text = message.chat
        print(text)
        if message.text == "да":
            await message.reply("ок", reply_markup=gym)
        if message.text != "да":
            await message.answer("Тогда нажмите Отель еще раз!")


@dp.message(F.text == "Парк")
async def ot(message: Message):
    house = [rasm10, rasm11, rasm12]
    n = random.choice(house)
    await message.answer_photo(f"{n}", caption="Вам понравилось этот Парк?")

    @dp.message()
    async def a(message: Message):
        text = message.chat
        print(text)
        if message.text == "да":
            await message.reply("ок", reply_markup=gym)
        if message.text != "да":
            await message.answer("Тогда нажмите Парк еще раз!")


@dp.message(F.text == "Samarqand")
async def sama(message: Message):
    await message.answer_photo(photo="https://unsplash.com/photos/green-and-brown-concrete-building-x-xwFxX2wVU", reply_markup=we,  caption="добро пожаловать в Самарканд"
                                                                                                                                                "\nчто ищете выберете 1 из 4")

    # @dp.message(F.text == "Кафе")
    # async def sama(message: Message):
    #     f = [rasm13, rasm14, rasm15]
    #     gen = random.choice(f)
    #     await message.answer_photo(f"{gen}", caption="Вам понравилось этот Кафе?")
    #
    #     @dp.message()
    #     async def bm(message: Message):
    #         text = message.chat
    #         print(text)
    #         if message.text == "да":
    #             await message.reply("ок", reply_markup=gym)
    #         if message.text != "да":
    #             await message.reply("Тогда нажмите кафе еще раз!")







async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


