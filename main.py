import asyncio
import logging
import random

from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from config import token
from image import *
from buttons import *
from inlinekey import *
from inlinkeyborard import *
from aiogram import Dispatcher, F, Bot

TOKEN = token

router = Router()
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer_photo(photo="https://www.istockphoto.com/photo/successful-partnership-gm1195021038-340485624", caption=f"{message.from_user.first_name}👋 : \nChoose your language!\n"
                         "Выберете язык чтобы продолжить!\n", reply_markup=gta)


@router.callback_query(lambda c: c.data == "Ale")
async def inline_button_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer_photo(photo="https://plus.unsplash.com/premium_photo-1679826780076-5926172bd6bf?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bG9jYXRpb24lMjBsb2dvfGVufDB8fDB8fHww", caption="на данный момент ваше местоположение🏙", reply_markup=hub)

@router.callback_query(lambda c: c.data == "Sms")
async def inline_button_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer_photo(photo="https://plus.unsplash.com/premium_photo-1679826780076-5926172bd6bf?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bG9jYXRpb24lMjBsb2dvfGVufDB8fDB8fHww", caption="Your current location🏙", reply_markup=git)




@dp.callback_query(F.data == "ss")
async def russ(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://media.istockphoto.com/id/2150829608/photo/scenic-view-from-a-quadcopter-of-the-largest-kazakh-city-of-almaty-in-the-early-spring-morning.jpg?s=1024x1024&w=is&k=20&c=DkAZx_h3YVm7sStvEJicTL8CwtedKBIuMWGM2wkMJ2k=", reply_markup=ubay, caption="👋добро пожаловать в Андижан"
                                                                                                                                                                                                                                                                                              "\n⛱что ищете выберете 1 из 4 ")

@dp.callback_query(F.data == "sss")
async def eng(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://media.istockphoto.com/id/2150829608/photo/scenic-view-from-a-quadcopter-of-the-largest-kazakh-city-of-almaty-in-the-early-spring-morning.jpg?s=1024x1024&w=is&k=20&c=DkAZx_h3YVm7sStvEJicTL8CwtedKBIuMWGM2wkMJ2k=", reply_markup=ubay1, caption="👋Welcome to Andijan"
                                                                                                                                                                                                                                                                                               "\n⛱choose what you need")



@dp.callback_query(F.data == "jum")
async def ca(callback: CallbackQuery):
    List = [rasm1, rasm2, rasm3]
    for x in List:
        await callback.message.answer_photo(f"{x}", caption="выберете 1 из 3?", reply_markup=build.as_markup())


@dp.callback_query(F.data == "jam")
async def ca(callback: CallbackQuery):
    List = [rasm1, rasm2, rasm3]
    for x in List:
        await callback.message.answer_photo(f"{x}", caption="choose", reply_markup=build3.as_markup())





@dp.callback_query(F.data == "gla")
async def res(callback: CallbackQuery):
    a = [rasm4, rasm5, rasm6]
    for x in a:
        await callback.message.answer_photo(f"{x}", caption="⛱Вот вам 3 Ресторана выберете понравишсья", reply_markup=build2.as_markup())

@dp.callback_query(F.data == "pubg")
async def res(callback: CallbackQuery):
    a = [rasm4, rasm5, rasm6]
    for x in a:
        await callback.message.answer_photo(f"{x}", caption="🍔choose 1 please?", reply_markup=build4.as_markup())




@dp.callback_query(F.data == "gtr")
async def ot(callback: CallbackQuery):
    uy = [rasm7, rasm8, rasm9]
    for x in uy:
        await callback.message.answer_photo(f"{x}", caption="🏝: выберете одну из 3?", reply_markup=ab.as_markup())

@dp.callback_query(F.data == "merss")
async def ress(callback: CallbackQuery):
    go = [rasm7, rasm8, rasm9]
    for x in go:
        await callback.message.answer_photo(f"{x}", caption="🏖choose 1 please?", reply_markup=gf.as_markup())




@dp.callback_query(F.data == "jump")
async def ot(callback: CallbackQuery):
    house = [rasm10, rasm11, rasm12]
    for x in house:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Парк?", reply_markup=ad.as_markup())

@dp.callback_query(F.data == "jumping")
async def res(callback: CallbackQuery):
    buy = [rasm10, rasm11, rasm12]
    for x in buy:
        await callback.message.answer_photo(f"{x}", caption="⛱choose 1 please?", reply_markup=gfk.as_markup())


# --------------------------------------------------------------------------------------------




@dp.callback_query(F.data == "самар")
async def samar(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://unsplash.com/photos/green-and-brown-concrete-building-x-xwFxX2wVU", reply_markup=uba2,  caption="добро пожаловать в Самарканд"
                                                                                                                                                "\nчто ищете выберете 1 из 4")

@dp.callback_query(F.data == "kafe")
async def sama(callback: CallbackQuery):
    f = [rasm13, rasm14, rasm15]
    for x in f:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Кафе?", reply_markup=samarqand.as_markup())


@dp.callback_query(F.data == "rest")
async def rest(callback: CallbackQuery):
    sama = [rasm16, rasm17, rasm18]
    for x in sama:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Ресторан", reply_markup=samarqandres.as_markup())



@dp.callback_query(F.data == "hote")
async def hot(callback: CallbackQuery):
    hot = [rasm19, rasm20, rasm21]
    for x in hot:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Отель", reply_markup=samarqandreshote.as_markup())



@dp.callback_query(F.data == "park")
async def park(callback: CallbackQuery):
    park = [rasm22, rasm23, rasm24]
    for x in park:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Парк", reply_markup=samarqandrespark.as_markup())

# ---------------------------------------------------------------------------------------------------------------------------


@dp.callback_query(F.data == "samar")
async def samar(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://unsplash.com/photos/green-and-brown-concrete-building-x-xwFxX2wVU", reply_markup=englishsama,  caption="Welcome to Samakand"
                                                                                                                                                "\nwhat you need please choose!")



@dp.callback_query(F.data == "cafe")
async def sama(callback: CallbackQuery):
    f = [rasm13, rasm14, rasm15]
    for x in f:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Cafe?", reply_markup=samarqandeng.as_markup())



@dp.callback_query(F.data == "restar")
async def rest(callback: CallbackQuery):
    sama = [rasm16, rasm17, rasm18]
    for x in sama:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Restaurant", reply_markup=samarqandengres.as_markup())





@dp.callback_query(F.data == "hotel")
async def hot(callback: CallbackQuery):
    hot = [rasm19, rasm20, rasm21]
    for x in hot:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Hotel", reply_markup=samarqandenghot.as_markup())


@dp.callback_query(F.data == "par")
async def park(callback: CallbackQuery):
    park = [rasm22, rasm23, rasm24]
    for x in park:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Park", reply_markup=samarqandengpark.as_markup())

# ----------------------------------------------------------------------------------------------------


@dp.callback_query(F.data == "хоразм")
async def xor(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcRdm3iEAETPV8tEIhfJa7o0ekijxhOHIW506hQAFGi7p5SO7pzMvE_q4Azgi10xTZfFoQiylQBIVeLqpIBQMOjVO5Jk7Qbjgmvg2eElTA", reply_markup=uba3, caption="Добро пожаловать Хоразм"
                                                                                                                                                                                                                                                   "\nВыберете 1 из 4")



@dp.callback_query(F.data == "cafee")
async def caf(callback: CallbackQuery):
    xor = [rasm25, rasm26, rasm27]
    for x in xor:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Кафе?", reply_markup=xorazmruscafe.as_markup())



@dp.callback_query(F.data == "resttt")
async def caf(callback: CallbackQuery):
    restt = [rasm28, rasm29, rasm30]
    for x in restt:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Ресторанам?", reply_markup=xorazmrusrestoran.as_markup())



@dp.callback_query(F.data == "hotell")
async def caf(callback: CallbackQuery):
    hotell = [rasm31, rasm32, rasm33]
    for x in hotell:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Отель?", reply_markup=xorazmrushotel.as_markup())


# -------------------------------------------------------------------------------------------------------------------


@dp.callback_query(F.data == "xorazm")
async def xor(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcRdm3iEAETPV8tEIhfJa7o0ekijxhOHIW506hQAFGi7p5SO7pzMvE_q4Azgi10xTZfFoQiylQBIVeLqpIBQMOjVO5Jk7Qbjgmvg2eElTA", reply_markup=uba4, caption="Welcome to Khorezm"
                                                                                                                                                                                                                                                   "\nchoose 1 please!")



@dp.callback_query(F.data == "caff")
async def caf(callback: CallbackQuery):
    xor = [rasm25, rasm26, rasm27]
    for x in xor:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Cafe?", reply_markup=xorazmengcafe.as_markup())



@dp.callback_query(F.data == "restttt")
async def caf(callback: CallbackQuery):
    restt = [rasm28, rasm29, rasm30]
    for x in restt:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Restaurant?", reply_markup=xorazmengrestoran.as_markup())




@dp.callback_query(F.data == "hotelll")
async def caf(callback: CallbackQuery):
    hotell = [rasm31, rasm32, rasm33]
    for x in hotell:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Hotel?", reply_markup=xorazmenghotel.as_markup())


# -----------------------------------------------------------------------------------------------------------------------


@dp.callback_query(F.data == "бухара")
async def xor(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcR_AYJ8aSdojU7FHgRy9UPKuw3rfQ34DvIaxAjDohwNN54NK_hxE3wxYQTpjOqQapfueCyvnP09SDXSzP9ZkJV6uH09PvPyVUZmefqR-g", reply_markup=uba5, caption="Добро пожаловать Бухара"
                                                                                                                                                                                                                                                   "\nВыберете 1 из 4")


@dp.callback_query(F.data == "Кафее")
async def caf(callback: CallbackQuery):
    bux = [rasm34, rasm35, rasm36]
    for x in bux:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Кафе?", reply_markup=buxororuscafe.as_markup())


@dp.callback_query(F.data == "ресторан")
async def caf(callback: CallbackQuery):
    bux = [rasm37, rasm38, rasm39]
    for x in bux:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Ресторанам?", reply_markup=buxororusrestoran.as_markup())


@dp.callback_query(F.data == "отель")
async def caf(callback: CallbackQuery):
    bux = [rasm40, rasm41, rasm42]
    for x in bux:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Отель?", reply_markup=buxororushotel.as_markup())


@dp.callback_query(F.data == "парк")
async def caf(callback: CallbackQuery):
    bux = [rasm43, rasm44, rasm45]
    for x in bux:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Парк?", reply_markup=buxororuspark.as_markup())


# -----------------------------------------------------------------------------------------------------------------


@dp.callback_query(F.data == "buxoro")
async def xor(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcR_AYJ8aSdojU7FHgRy9UPKuw3rfQ34DvIaxAjDohwNN54NK_hxE3wxYQTpjOqQapfueCyvnP09SDXSzP9ZkJV6uH09PvPyVUZmefqR-g", reply_markup=uba6, caption="Welcome to the Buxkara"
                                                                                                                                                                                                                                                   "\nChoose 1 pleaase!")


@dp.callback_query(F.data == "Кафееe")
async def caf(callback: CallbackQuery):
    bux = [rasm34, rasm35, rasm36]
    for x in bux:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Cafe?", reply_markup=buxoroengcafe.as_markup())



@dp.callback_query(F.data == "ресторанn")
async def caf(callback: CallbackQuery):
    bux = [rasm37, rasm38, rasm39]
    for x in bux:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Restaurant?", reply_markup=buxoroengrestoran.as_markup())



@dp.callback_query(F.data == "отельg")
async def caf(callback: CallbackQuery):
    bux = [rasm40, rasm41, rasm42]
    for x in bux:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Hotel?", reply_markup=buxoroenghotel.as_markup())



@dp.callback_query(F.data == "паркr")
async def caf(callback: CallbackQuery):
    bux = [rasm43, rasm44, rasm45]
    for x in bux:
        await callback.message.answer_photo(f"{x}", caption="Do you prefer Park?", reply_markup=buxoroengpark.as_markup())

# -----------------------------------------------------------------------------------------------------------------


@dp.callback_query(F.data == "ташкент")
async def tash(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcR7aAyCmkJEAjiorq-CttzImvKbiXWm-8k417LaK0a3S-y9gZ3cSLIl1FOnpmvvvLOyQbpVZwgM-ilw_BztgPtsAfLqeHmVjMoQLOiipFg", reply_markup=uba7, caption="Добро пожаловать Ташкент"
                                                                                                                                                                                                                                                   "\nВыберете 1 из 4")



@dp.callback_query(F.data == "coft")
async def tash(callback: CallbackQuery):
    tash = [rasm46, rasm47, rasm48]
    for x in tash:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Кафе", reply_markup=tashkentruscafe.as_markup())



@dp.callback_query(F.data == "restart")
async def tash(callback: CallbackQuery):
    tash =[rasm49, rasm50, rasm51]
    for x in tash:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Ресторан", reply_markup=tashkentrusrestoran.as_markup())


@dp.callback_query(F.data == "hostel")
async def tash(callback: CallbackQuery):
    tash =[rasm52, rasm53, rasm54]
    for x in tash:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Отель", reply_markup=tashkentrushotel.as_markup())




@dp.callback_query(F.data == "parl")
async def tash(callback: CallbackQuery):
    tash =[rasm55, rasm56, rasm57]
    for x in tash:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Парк", reply_markup=tashkentruspark.as_markup())


# -------------------------------------------------------------------------


@dp.callback_query(F.data == "tashkent")
async def tashk(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcR7aAyCmkJEAjiorq-CttzImvKbiXWm-8k417LaK0a3S-y9gZ3cSLIl1FOnpmvvvLOyQbpVZwgM-ilw_BztgPtsAfLqeHmVjMoQLOiipFg", reply_markup=uba8, caption="✋Welcome to the Tashkent"
                                                                                                                                                                                                                                                    "\n❓Choose what you need?")




@dp.callback_query(F.data == "cofter")
async def tash(callback: CallbackQuery):
    tash = [rasm46, rasm47, rasm48]
    for x in tash:
        await callback.message.answer_photo(f"{x}", caption="Did you like this one Cafe", reply_markup=tashkentengcafe.as_markup())


@dp.callback_query(F.data == "restarttt")
async def tash(callback: CallbackQuery):
    tash =[rasm49, rasm50, rasm51]
    for x in tash:
        await callback.message.answer_photo(f"{x}", caption="Did you like this one Restaurant", reply_markup=tashkentengrestoran.as_markup())



@dp.callback_query(F.data == "hostelel")
async def tash(callback: CallbackQuery):
    tash =[rasm52, rasm53, rasm54]
    for x in tash:
        await callback.message.answer_photo(f"{x}", caption="Did you like this one Hotel", reply_markup=tashkentenghotel.as_markup())



@dp.callback_query(F.data == "parol")
async def tash(callback: CallbackQuery):
    tash =[rasm55, rasm56, rasm57]
    for x in tash:
        await callback.message.answer_photo(f"{x}", caption="Did you like this one Park", reply_markup=tashkentengpark.as_markup())


# -------------------------------------------------------------


@dp.callback_query(F.data == "наманган")
async def nam(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://lh5.googleusercontent.com/p/AF1QipMl7TZaeWnLz3kJfNYFd9bMLe55yLU8Dx5DKANs=w540-h312-n-k-no", reply_markup=uba9, caption="Добро пожаловать в Наманган"
                                                                                                                                                                              "\nВыберете 1 из 4!")



@dp.callback_query(F.data == "jafe")
async def nam(callback: CallbackQuery):
    nam = [rasm58, rasm59, rasm60]
    for x in nam:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот кафе", reply_markup=namanganruscafe.as_markup())



@dp.callback_query(F.data == "jestoran")
async def nam(callback: CallbackQuery):
    nam = [rasm61, rasm62, rasm63]
    for x in nam:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Ресторан", reply_markup=namanganrusrestoran.as_markup())



@dp.callback_query(F.data == "jostel")
async def hot(callback: CallbackQuery):
    nam = [rasm64, rasm65, rasm66]
    for x in nam:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Отель", reply_markup=namanganrushotel.as_markup())


@dp.callback_query(F.data == "jark")
async def hot(callback: CallbackQuery):
    nam = [rasm67, rasm68, rasm69]
    for x in nam:
        await callback.message.answer_photo(f"{x}", caption="Вам понравилось этот Парк", reply_markup=namanganruspark.as_markup())


# ---------------------------------------------------------------------------------------------------------------------------


@dp.callback_query(F.data == "namangan")
async def nam(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://lh5.googleusercontent.com/p/AF1QipMl7TZaeWnLz3kJfNYFd9bMLe55yLU8Dx5DKANs=w540-h312-n-k-no", reply_markup=namanganeng, caption="Welcome to the Namangan"
                                                                                                                                                                              "\nChoose what you need!")



@dp.callback_query(F.data == "jafee")
async def nam(callback: CallbackQuery):
    nam = [rasm58, rasm59, rasm60]
    for x in nam:
        await callback.message.answer_photo(f"{x}", caption="Did you like this one Cafe", reply_markup=namanganengcafe.as_markup())



@dp.callback_query(F.data == "jestorann")
async def nam(callback: CallbackQuery):
    nam = [rasm61, rasm62, rasm63]
    for x in nam:
        await callback.message.answer_photo(f"{x}", caption="Did you like this one Restaurant", reply_markup=namanganengrestoran.as_markup())


@dp.callback_query(F.data == "jostell")
async def hot(callback: CallbackQuery):
    nam = [rasm64, rasm65, rasm66]
    for x in nam:
        await callback.message.answer_photo(f"{x}", caption="Did you like this one Hotel", reply_markup=namanganenghotel.as_markup())



@dp.callback_query(F.data == "jarkk")
async def hot(callback: CallbackQuery):
    nam = [rasm67, rasm68, rasm69]
    for x in nam:
        await callback.message.answer_photo(f"{x}", caption="Did you like this one Park", reply_markup=namanganengpark.as_markup())






dp.include_router(router)

async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


