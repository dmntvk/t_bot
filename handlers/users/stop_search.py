from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import kb_menu
from utils.misc import rate_limit
from utils.dbapi import quick_commands


@rate_limit(limit=15)


@dp.message_handler(text='❌️ Остановить поиск')
async def command_start(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        await quick_commands.del_queue(user_id=message.from_user.id)
        await message.answer(f'Поиск игры остановлен ❌️ \n'
                             f'\n', parse_mode='html', reply_markup=kb_menu)
        await quick_commands.del_queue(message.from_user.id)
    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')