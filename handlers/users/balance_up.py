from aiogram import types
from loader import dp
from keyboards.inline.inline import b_up_menu, oplata
from keyboards.default.keyboard_menu import kb_menu
from utils.misc import rate_limit
from utils.dbapi import quick_commands
import random
from data.config import p2p


@rate_limit(limit=15)
@dp.message_handler(text='📥 Пополнить баланс')
async def command_error(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        await message.answer(f'Выберете сумму пополнения:\n', parse_mode='html', reply_markup=b_up_menu)
    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')

@dp.callback_query_handler(text='10')
async def sum10(message: types.CallbackQuery):
    amount = 10
    await message.message.delete()
    comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
    bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
    await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
    await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi\n'
                         f'', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))

@dp.callback_query_handler(text='25')
async def sum10(message: types.CallbackQuery):
    amount = 25
    await message.message.delete()
    comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
    bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
    await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
    await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi\n'
                         f'', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))

@dp.callback_query_handler(text='50')
async def sum10(message: types.CallbackQuery):
    amount = 50
    await message.message.delete()
    comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
    bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
    await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
    await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi\n'
                         f'', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))

@dp.callback_query_handler(text='100')
async def sum10(message: types.CallbackQuery):
    amount = 100
    await message.message.delete()
    comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
    bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
    await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
    await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi\n'
                         f'', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))

@dp.callback_query_handler(text='250')
async def sum10(message: types.CallbackQuery):
    amount = 250
    await message.message.delete()
    comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
    bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
    await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
    await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi\n'
                         f'', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))

@dp.callback_query_handler(text='500')
async def sum10(message: types.CallbackQuery):
    amount = 500
    await message.message.delete()
    comment = str(message.from_user.id) + '_' + str(random.randint(1000, 9999999))
    bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
    await quick_commands.create_check(user_id=message.from_user.id, amount=amount, bill_id=bill.bill_id, url_p=bill.pay_url)
    await message.message.answer(f'Вам нужно отправить {amount}₽ на наш счет Qiwi\n'
                         f'', reply_markup=oplata(url=bill.pay_url, bill=bill.bill_id))

@dp.callback_query_handler(text_contains='check_')
async def check(callback: types.CallbackQuery):
    bill = str(callback.data[6:])
    info = await quick_commands.get_check(bill_id=bill)
    if info != False:
        if str(p2p.check(bill_id=bill).status) == 'PAID':
            await callback.message.delete()
            await quick_commands.deposit_balance(user_id=callback.from_user.id, amount=float(info.amount))
            await callback.message.answer(f'Ваш счет успешно пополнен на {info.amount}₽', reply_markup=kb_menu)
            await quick_commands.del_check(bill_id=bill)
        else:
            await callback.message.delete()
            await dp.bot.send_message(callback.from_user.id, 'Вы не оплатили счет!', reply_markup=oplata(url=info.url_p, bill=bill))
    else:
        await dp.bot.send_message(callback.from_user.id, 'Счет не найден')

@dp.callback_query_handler(text_contains='cancel')
async def delceck(callback: types.CallbackQuery):
    bill = str(callback.data[6:])
    await quick_commands.del_check(bill_id=bill)
    await callback.message.delete()
    await callback.message.answer('Счет на оплату удален!', reply_markup=kb_menu)