from aiogram import types
from loader import dp
from keyboards.inline.inline import bns_menu
from keyboards.default.keyboard_menu import kb_menu
from utils.misc import rate_limit
from utils.dbapi import quick_commands



@rate_limit(limit=15)
@dp.message_handler(text='🎁 Бонус')
async def command_error(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        await message.answer(f'Чтобы получить бонус вам нужно подписаться на наш Telegram канал!\n'
                             f'В нем каждый день будут публиковаться промокоды!', parse_mode='html', reply_markup=bns_menu)

    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')


@dp.callback_query_handler(text='checks_sub')
async def check_sub_channel(callbacl: types.CallbackQuery):
    chat_member = await callbacl.bot.get_chat_member(chat_id=-1001871426229, user_id=callbacl.from_user.id)
    if chat_member['status'] == 'left':
        await callbacl.message.delete()
        await callbacl.message.answer('Вы не подписались на канал!', reply_markup=bns_menu)
    else:
        check = await quick_commands.bonus_check(callbacl.from_user.id)
        if check == True:
            await callbacl.message.delete()
            await quick_commands.bonus_active(callbacl.from_user.id)
            await callbacl.message.answer('Вы успешно получили на свой счет 25₽!', reply_markup=kb_menu)
        else:
            await callbacl.message.delete()
            await callbacl.message.answer('Вы уже получили данный вид бонуса!', reply_markup=kb_menu)