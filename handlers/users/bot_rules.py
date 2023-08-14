from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import kb_menu
from utils.misc import rate_limit
from utils.dbapi import quick_commands


@rate_limit(limit=15)
@dp.message_handler(text='/rules')
async def command_error(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        await message.answer(f'<strong>Правила игры:</strong>\n'
                             f'Ножницы режут бумагу.\n'
                             f'Бумага заворачивает камень.\n'
                             f'Камень ломает ножницы.', parse_mode='html', reply_markup=kb_menu)

    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')