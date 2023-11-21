from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.methods.forward_message import ForwardMessage
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery

import config
from states import Myquery
import kb
import text
import db

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):

    user_id = msg.from_user.id
    user_name = msg.from_user.username
    user_full_name = msg.from_user.full_name
    user_exists = await db.check_user_exists(user_id)

    if user_exists:
        #await msg.answer(text.comeback.format(name=msg.from_user.full_name))
        await msg.reply(text.comeback.format(name=msg.from_user.full_name),reply_markup=kb.menu)
    else:
       # await db.add_new_user(user_id, user_name, user_full_name)
        await msg.reply(text.hi.format(name=msg.from_user.full_name), reply_markup=kb.startmenu)


@router.message(lambda message: message.contact is not None)
async def send_contact(msg: Message):
    print(msg.contact)
    # написать функцию которая отправлет данные о запросе в другой чат
    #await msg.send_message(chat_id='ID или название чата', text=msg.contact)
    #await msg.forward(chat_id=config.ADMINISTRATOR_CHANNEL_ID)
    await msg.answer(text.send_query.format(name=msg.from_user.full_name))


@router.message(F.text =="Узнать статус заявки")
async def my_status(msg: Message):
    user_id = msg.from_user.id
    user_exists = await db.check_user_exists(user_id)
    if user_exists:
        await msg.answer(text.comeback.format(name=msg.from_user.full_name))
    else:
        await msg.answer(text.status_wait, reply_markup=kb.startmenu)


@router.message(F.text == "Заявки на ремонт")
async def repair_requests(msg: Message):
    user_id = msg.from_user.id
    user_exists = await db.check_user_exists(user_id)
    if user_exists:
        await msg.answer(text.problems, reply_markup=kb.problems.as_markup(resize_keyboard=True))
    else:
        await msg.answer(text.hi.format(name=msg.from_user.full_name), reply_markup=kb.startmenu)

@router.message(F.text == "Мои задачи")
async def my_tasks(msg: Message):
    user_id = msg.from_user.id
    user_exists = await db.check_user_exists(user_id)
    if user_exists:
        await msg.answer(text.tasks, reply_markup=kb.tasks.as_markup(resize_keyboard=True))
    else:
        await msg.answer(text.hi.format(name=msg.from_user.full_name), reply_markup=kb.startmenu)

@router.message(F.text == "Меню")
@router.message(F.text == "Menu")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)
#
# @router.callback_query(F.text == "Да, срочный")
# async def send_query(clbck: CallbackQuery, state: FSMContext):
#     await state.set_state(Myquery.send_query)
#
#     #await clbck.message.edit_text(text.send_query)
#     await clbck.message.answer(text.send_query, reply_markup=kb.startmenu)


#
# @router.callback_query(F.data == "report_problem")
# async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
#     await state.set_state(Task.problem_text)
#     await clbck.message.edit_text(text.in_problem)
#     await clbck.message.answer(text.or_back, reply_markup=kb.exit_kb)

#
# @router.message(Task.problem_text)
# async def save_text(msg: Message, state: FSMContext):
#     user_id = msg.from_user.id
#     cur_date = msg.date.date()
#     cur_time = msg.date.time()
#     problem = msg.text
#     await db.create_send_problems()
#     await db.add_new_problem(user_id,cur_date, cur_time, problem, status=True)
#     await msg.answer(text.out_problem, reply_markup=kb.exit_kb, disable_web_page_preview=True)


#
# @router.message(Task.no_input)
# async def message_handler(msg: Message, state: FSMContext):
#     # Устанавливаем фильтр для блокировки текстовых сообщений
#
#     if msg.content_type == "text":
#
#         await msg.answer(text.free_text)