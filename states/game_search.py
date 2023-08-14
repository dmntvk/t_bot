
from aiogram.dispatcher.filters.state import StatesGroup, State

class Game(StatesGroup):
     game_id = State()
     amount = State()