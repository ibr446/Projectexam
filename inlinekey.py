from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

build = InlineKeyboardBuilder()

build.add(types.InlineKeyboardButton(
    text="Локация", url="https://maps.app.goo.gl/3uQtjQhZFELXqLASA")
)
build.add(types.InlineKeyboardButton(
    text="Контакт📞", url="https://google.com",
))

# menu = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Локация", url="https://maps.app.goo.gl/garSTG3fD3uEnkK39")]    ]
# )
#
#
# menu2 = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Локация", url="https://maps.app.goo.gl/hckTnoPKUxis6xBb6")]
#     ]
# )



location = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Локация", callback_data="lok", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")],
    [InlineKeyboardButton(text="Контакт", callback_data="kont", url="https://google.com")],
])

location2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Локация", callback_data="lokk", url="https://maps.app.goo.gl/VzkUNtk9xVWkJcfy6")],
    [InlineKeyboardButton(text="Контакт", callback_data="kontt", url="https://google.com")],
])



build2 = InlineKeyboardBuilder()

build2.add(types.InlineKeyboardButton(
    text="Локация🚨", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

build2.add(types.InlineKeyboardButton(
    text="Контакт📞", url="https://google.com",
))





build3 = InlineKeyboardBuilder()

build3.add(types.InlineKeyboardButton(
    text="Location🚨", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

build3.add(types.InlineKeyboardButton(
    text="Contact📞", url="https://google.com"
))




build4 = InlineKeyboardBuilder()

build4.add(types.InlineKeyboardButton(
    text="Location", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

build4.add(types.InlineKeyboardButton(
    text="Contact", url="https://google.com"
))



ab = InlineKeyboardBuilder()

ab.add(types.InlineKeyboardButton(
    text="Локация", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

ab.add(types.InlineKeyboardButton(
    text="Контакт", url="https://google.com"
))




gf = InlineKeyboardBuilder()

gf.add(types.InlineKeyboardButton(
    text="Location", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

gf.add(types.InlineKeyboardButton(
    text="Contact", url="https://google.com"
))





ad = InlineKeyboardBuilder()

ad.add(types.InlineKeyboardButton(
    text="Локация", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

ad.add(types.InlineKeyboardButton(
    text="Контакт", url="https://google.com"
))



gfk = InlineKeyboardBuilder()

gfk.add(types.InlineKeyboardButton(
    text="Location", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

gfk.add(types.InlineKeyboardButton(
    text="Contact", url="https://google.com"
))





samarqand = InlineKeyboardBuilder()

samarqand.add(types.InlineKeyboardButton(
    text="Локация🚨", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

samarqand.add(types.InlineKeyboardButton(
    text="Контакт📞", url="https://google.com"
))




engsama = InlineKeyboardBuilder()

engsama.add(types.InlineKeyboardButton(
    text="Location🚨", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

engsama.add(types.InlineKeyboardButton(
    text="Contact📞", url="https://google.com"
))




rusxor = InlineKeyboardBuilder()

rusxor.add(types.InlineKeyboardButton(
    text="Локация🚨", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

rusxor.add(types.InlineKeyboardButton(
    text="Контакт📞", url="https://google.com"
))



engxor = InlineKeyboardBuilder()

engxor.add(types.InlineKeyboardButton(
    text="Location🚨", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

engxor.add(types.InlineKeyboardButton(
    text="Contact📞", url="https://google.com"
))


rusbuxor = InlineKeyboardBuilder()

rusbuxor.add(types.InlineKeyboardButton(
    text="Локация🚨", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

rusbuxor.add(types.InlineKeyboardButton(
    text="Контакт📞", url="https://google.com"
))



engbuxor = InlineKeyboardBuilder()

engbuxor.add(types.InlineKeyboardButton(
    text="Location🚨", url="https://maps.app.goo.gl/oQoMhizoiw36dE1k9")
)

engbuxor.add(types.InlineKeyboardButton(
    text="Contact📞", url="https://google.com"
))





gta = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Russian🇷🇺", callback_data="Ale")],
    [InlineKeyboardButton(text="English🇺🇸", callback_data="Sms")],
])


hub = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Андижан📍", callback_data="ss")],
    [InlineKeyboardButton(text="Самарканд📍", callback_data="самар")],
    [InlineKeyboardButton(text="Харазим📍", callback_data="хоразм")],
    [InlineKeyboardButton(text="Бухара📍", callback_data="бухара")],
    [InlineKeyboardButton(text="Ташкент📍", callback_data="ташкент")],
    [InlineKeyboardButton(text="Наманган📍", callback_data="наманган")]
])



git = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Andijan📍", callback_data="sss")],
    [InlineKeyboardButton(text="Samarkand📍", callback_data="samar")],
    [InlineKeyboardButton(text="Khorezm📍", callback_data="xorazm")],
    [InlineKeyboardButton(text="Bukhara📍", callback_data="buxoro")],
    [InlineKeyboardButton(text="Tashkent📍", callback_data="tashkent")],
    [InlineKeyboardButton(text="Namangan📍", callback_data="namangan")]
])


ubay = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кафе☕️", callback_data="jum")],
    [InlineKeyboardButton(text="Ресторан🍔", callback_data="gla")],
    [InlineKeyboardButton(text="Отель🏝", callback_data="gtr")],
    [InlineKeyboardButton(text="Парк🎡", callback_data="jump")]
])



ubay1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Cafe☕️", callback_data="jam")],
    [InlineKeyboardButton(text="Restaurant🍔", callback_data="pubg")],
    [InlineKeyboardButton(text="Hotel🏝", callback_data="merss")],
    [InlineKeyboardButton(text="Park🎡", callback_data="jumping")]
])




uba2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кафе☕️", callback_data="kafe")],
    [InlineKeyboardButton(text="Ресторан🍔", callback_data="rest")],
    [InlineKeyboardButton(text="Отель🏝", callback_data="hote")],
    [InlineKeyboardButton(text="Парк🎡", callback_data="park")]
])


englishsama = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="cafe☕️", callback_data="cafe")],
    [InlineKeyboardButton(text="Restaurant🍔", callback_data="restar")],
    [InlineKeyboardButton(text="Hotel🏝", callback_data="hotel")],
    [InlineKeyboardButton(text="Park🎡", callback_data="par")]
])



uba3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кафе☕️", callback_data="cafee")],
    [InlineKeyboardButton(text="Ресторан🍔", callback_data="resttt")],
    [InlineKeyboardButton(text="Отель🏝", callback_data="hotell")],
])

uba4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Cafe☕️", callback_data="caff")],
    [InlineKeyboardButton(text="Restaurant🍔", callback_data="restttt")],
    [InlineKeyboardButton(text="Hotel🏝", callback_data="hotelll")],
])



uba5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кафе☕️", callback_data="Кафее")],
    [InlineKeyboardButton(text="Ресторан🍔", callback_data="ресторан")],
    [InlineKeyboardButton(text="Отель🏝", callback_data="отель")],
    [InlineKeyboardButton(text="Парк🎡", callback_data="парк")]
])


uba6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="cafe☕️", callback_data="Кафееe")],
    [InlineKeyboardButton(text="Restaurant🍔", callback_data="ресторанn")],
    [InlineKeyboardButton(text="Hotel🏝", callback_data="отельg")],
    [InlineKeyboardButton(text="Park🎡", callback_data="паркr")]
])



uba7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кафе☕️", callback_data="coft")],
    [InlineKeyboardButton(text="Ресторан🍔", callback_data="restart")],
    [InlineKeyboardButton(text="Отель🏝", callback_data="hostel")],
    [InlineKeyboardButton(text="Парк🎡", callback_data="parl")]
])


uba8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кафе☕️", callback_data="coft")],
    [InlineKeyboardButton(text="Ресторан🍔", callback_data="restart")],
    [InlineKeyboardButton(text="Отель🏝", callback_data="hostel")],
    [InlineKeyboardButton(text="Парк🎡", callback_data="parl")]
])





















































































