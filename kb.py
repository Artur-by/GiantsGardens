from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,\
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# inline_startmenu = [
#     [InlineKeyboardButton(text="Узнать статус заявки", callback_data="find_tasks"),
#     InlineKeyboardButton(text="Отправить запрос", callback_data="report_problem")]
# ]

reply_startmenu = [
    [KeyboardButton(text="Узнать статус заявки"),
    KeyboardButton(text="Отправить запрос", request_contact=True)
    ]
]


reply_menu = [
    [KeyboardButton(text="Мои задачи"),
    KeyboardButton(text="Заявки на ремонт")
     ]
]

problems = ReplyKeyboardBuilder()
problems.row(KeyboardButton(text="Да, срочный"), KeyboardButton(text="Нет, не срочный"))
problems.row(KeyboardButton(text="◀️ Выйти в меню"))

tasks = ReplyKeyboardBuilder()
tasks.row(KeyboardButton(text="Не закрытые"),KeyboardButton(text="Плановые"), KeyboardButton(text="Аварийные"))
tasks.row(KeyboardButton(text="◀️ Выйти в меню"))


startmenu = ReplyKeyboardMarkup(keyboard=reply_startmenu,  resize_keyboard=True)
menu = ReplyKeyboardMarkup(keyboard=reply_menu, resize_keyboard=True)

# startmenu = InlineKeyboardMarkup(inline_keyboard=startmenu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

