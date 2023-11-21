from aiogram.fsm.state import StatesGroup, State

class Myquery(StatesGroup):
    send_query = State()
    check_status = State()