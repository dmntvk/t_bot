from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import kb_menu
from utils.misc import rate_limit
from states import balance
from utils.dbapi import quick_commands


@rate_limit(limit=15)

@dp.message_handler(text='📥️ Пополнить')
async def command_balance(message: types.Message):
    await message.answer(f'Введите сумму пополнения баланса: \n', parse_mode='html', reply_markup=kb_menu)
    await balance.amount.set()

@dp.message_handler(state=balance.amount)
async def command_balance(message: types.Message):
    answer = message.text
    check_balance = await quick_commands.check_balance(user_id=message.from_user.id, answer=answer)
    if check_balance == 'no money':
        await message.answer()