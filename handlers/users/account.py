from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import ac_menu
from utils.misc import rate_limit
from utils.dbapi import quick_commands

@rate_limit(limit=15)

@dp.message_handler(text='⚙️ Аккаунт')
async def command_start(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    count_ref = await quick_commands.count_refs(message.from_user.id)
    if user.status == 'active':
        await message.answer(f'<strong>Мой аккаунт</strong>\n'
                             f'<em>Вся необходимая информация о вашем профиле</em>\n'
                             f'\n'
                             f'👤 <strong>ID: </strong>{user.user_id}\n'
                             f'💶 <strong>Баланс: {user.balance}</strong>\n'
                             f'👤 <strong>Регистрация: </strong>{user.created_at}\n'
                             f'👨‍👦‍👦 <strong>Рефералы: </strong>{count_ref}\n'
                             f'\n'
                             f'\n'
                             f'<strong>📝 Статистика Ваших игр</strong>\n'
                             f'├🎮 <strong>Всего игр: </strong>{user.all_game}\n'
                             f'├🏆 <strong>Побед: </strong>{user.win_game}\n'
                             f'└👁‍🗨 <strong>Проиграно игр: </strong>{user.luss_game}'

                             , parse_mode='html', reply_markup=ac_menu)
    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')