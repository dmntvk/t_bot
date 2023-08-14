from aiogram.dispatcher.filters.state import StatesGroup, State

class WithdrawalState(StatesGroup):
     qiwi = State()
     amount = State()