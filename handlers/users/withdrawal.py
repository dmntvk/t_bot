from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import wndrbl_menu, promo_menu, kb_menu
from keyboards.inline.inline import create_w_menu
from utils.misc import rate_limit
from utils.dbapi import quick_commands
from aiogram.dispatcher import FSMContext
from states.withdrawal_state import WithdrawalState


@rate_limit(limit=15)
@dp.message_handler(text='📤 Вывод средств')
async def withdrawal_menu(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        user_withdrawal = await quick_commands.faunds_withdrawal(user_id=message.from_user.id)
        if user_withdrawal == False:
            await message.answer(f'<strong>Текущая заявка на вывод средств:</strong>\n'
                                 f'· У вас нет текущих заявок на вывод средств', parse_mode='html', reply_markup=wndrbl_menu)

        else:
            await message.answer(f'<strong>Текущая заявка на вывод средств:</strong>\n'
                                 f' · ID заявки: <code>{user_withdrawal.id}</code>\n'
                                 f' · Сумма вывода: <code>{user_withdrawal.amount}₽</code>\n'
                                 f' · Статус заявки: <code>На рассмотрении ⌛</code>\n', parse_mode='html', reply_markup=kb_menu)
    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')

@dp.message_handler(text='🔙 Вернуться')
async def back_men(message: types.Message):
    await message.answer('Выберите действие:', reply_markup=kb_menu)

@dp.message_handler(text='📲 Создать заявку')
async def withdrawal_create(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        await message.answer('<strong>Создание заявки на вывод!</strong>\n'
                       'Выберете платежную систему:\n', reply_markup=create_w_menu)
    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')

@dp.callback_query_handler(text='qiwi')
async def create_withdrawal(callback: types.CallbackQuery):
    user = await quick_commands.select_user(callback.from_user.id)
    if user.status == 'active':
        await callback.message.delete()
        await callback.message.answer('<strong>Создание заявки на вывод средств на Qiwi!</strong>\n'
                                      'Укажите номер Qiwi:', reply_markup=promo_menu)
        await WithdrawalState.qiwi.set()
    if user.status == 'ban':
        await callback.message.answer('Вы заблокированы за махинации')

@dp.message_handler(state=WithdrawalState.qiwi)
async def wth_qiwi(message: types.Message, state: FSMContext):
    async with state.proxy() as qiwi_n:
        qiwi_n['qiwi'] = message.text
        if qiwi_n['qiwi'] == '🔙 Назад':
            await state.finish()
            await message.answer('Выберите действие:', reply_markup=kb_menu)
        else:
            await message.answer('<strong>Введите сумму вывода</strong>(минимальный порог 500₽)', reply_markup=promo_menu)
            await WithdrawalState.amount.set()

@dp.message_handler(state=WithdrawalState.amount)
async def wth_qiwi(message: types.Message, state: FSMContext):
    user = await quick_commands.select_user(message.from_user.id)
    async with state.proxy() as qiwi_n:
        qiwi_n['amount'] = message.text
        am = qiwi_n['amount'].isdigit()
        if qiwi_n['amount'] == '🔙 Назад':
            await state.finish()
        if am == False:
                        if qiwi_n['amount'] == '🔙 Назад':
                            await message.answer('Выберите действие:', reply_markup=kb_menu)
                            await state.finish()
                        else:
                            await message.answer(f'Сумму вывода нужно указать цифрами!\n'
                                                 f'<strong>Введите сумму вывода</strong>(минимальный порог 500₽)', reply_markup=promo_menu)
        if am == True:
            if int(qiwi_n['amount']) >= 500:
                if user.balance >= int(qiwi_n['amount']):
                    await state.finish()
                    await quick_commands.create_withdrawal(user_id=message.from_user.id, amount=int(qiwi_n['amount']), requisites=qiwi_n['qiwi'])
                    await message.answer(f'<strong>Заявка на вывод средств успешно создана!</strong>\n'
                                            f'Среднее время ожидания вывода средств <strong>от 1 часа до 3 дней</strong>', reply_markup=kb_menu)
                if user.balance < int(qiwi_n['amount']):
                    await message.answer(f'У вас не достаточно средств для вывода данной суммы!', reply_markup=kb_menu)
                    await state.finish()
            if int(qiwi_n['amount']) <= 499:
                            await message.answer(f'<strong>Минимальная сумма вывода 500₽!</strong>\n'
                                                 f'Укажите сумму вывода от 500₽:', reply_markup=promo_menu)
                            if qiwi_n['amount'] == '🔙 Назад':
                                await message.answer('Выберите действие:', reply_markup=kb_menu)
                                await state.finish()
