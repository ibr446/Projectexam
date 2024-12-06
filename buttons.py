from aiogram import types

key = [
    [types.KeyboardButton(text="Russian"), types.KeyboardButton(text="English")]

]
keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)




a = [
    [types.KeyboardButton(text="Andijon"), types.KeyboardButton(text="Samarqand")],
    [types.KeyboardButton(text="Qashqadaryo"), types.KeyboardButton(text="Navoiy")],
    [types.KeyboardButton(text="Toshkent"), types.KeyboardButton(text="Namangan")],
    [types.KeyboardButton(text="Farg'ona"), types.KeyboardButton(text="Buxoro")],
    [types.KeyboardButton(text="Surxandaryo"), types.KeyboardButton(text="Qo'qon")]
]
f = types.ReplyKeyboardMarkup(keyboard=a, resize_keyboard=True)




d = [
    [types.KeyboardButton(text="Cafe"), types.KeyboardButton(text="Restoran")],
    [types.KeyboardButton(text="Hotel"), types.KeyboardButton(text="Park")],
]
g = types.ReplyKeyboardMarkup(keyboard=d, resize_keyboard=True)



h = [
    [types.KeyboardButton(text="Location"), types.KeyboardButton(text="Contact")],
    [types.KeyboardButton(text="Back")]
]
golf = types.ReplyKeyboardMarkup(keyboard=h, resize_keyboard=True)




