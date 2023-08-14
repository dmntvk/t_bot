from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import kb_menu
from utils.misc import rate_limit
from utils.dbapi import quick_commands


@rate_limit(limit=15)
@dp.message_handler()
async def command_error(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        await message.answer(f'Такой команды нет в моем функционале 😭\n', parse_mode='html')

    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')