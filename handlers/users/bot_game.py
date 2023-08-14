from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import search_menu, knb_menu, faunds_menu
from keyboards.inline.inline import game_menu, kbm_amount_menu
from utils.misc import rate_limit
from utils.dbapi import quick_commands
from states import game_search
from aiogram.dispatcher import FSMContext
from states.knb_error import Game

@rate_limit(limit=15)


@dp.message_handler(text='🔎 Поиск игры')
async def command_start(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        await message.answer(f'Выберите игру в котору вы хотите сыграть:\n'
                             f'\n', parse_mode='html', reply_markup=game_menu)
    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')

@dp.callback_query_handler(text='🗿 Камень, ✂️ ножницы, 📝 бумага')
async def kbm_start(message: types.CallbackQuery):
    await message.message.edit_text(f'Выберите cумму на каторую вы хотите сыграть:\n'
                            f'\n', parse_mode='html', reply_markup=kbm_amount_menu)

@dp.callback_query_handler(text='10/1')
async def amount_game(message: types.CallbackQuery):
    amount = 10
    await message.message.delete()
    user = await quick_commands.select_user(message.from_user.id)
    if user.balance >= 10.0:
        get_game = await quick_commands.get_game(user_id=message.from_user.id, amount=amount)
        if get_game == False:
            await message.message.answer(f'Идет поиск игры ⌛\n'
                                            f'\n', parse_mode='html', reply_markup=search_menu)
            await quick_commands.add_queue(user_id=message.from_user.id, amount=amount)
        else:
            await quick_commands.get_history(user_id=message.from_user.id, amount=amount)
            await quick_commands.del_queue(message.from_user.id)
            await quick_commands.del_queue(get_game)
            await message.message.answer(f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=message.from_user.id, amount=amount)
            await message.bot.send_message(get_game, f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=get_game, amount=amount)
    elif user.balance <= 9.9:
        await message.message.answer(f'У Вас не достаточно средств для игры, пополните баланс!\n'
                                     f'\n', parse_mode='html', reply_markup=faunds_menu)

@dp.callback_query_handler(text='25/1')
async def amount_game(message: types.CallbackQuery):
    amount = 25
    await message.message.delete()
    user = await quick_commands.select_user(message.from_user.id)
    if user.balance >= 25.0:
        get_game = await quick_commands.get_game(user_id=message.from_user.id, amount=amount)
        if get_game == False:
            await message.message.answer(f'Идет поиск игры ⌛\n'
                                            f'\n', parse_mode='html', reply_markup=search_menu)
            await quick_commands.add_queue(user_id=message.from_user.id, amount=amount)
        else:
            await quick_commands.get_history(user_id=message.from_user.id, amount=amount)
            await quick_commands.del_queue(message.from_user.id)
            await quick_commands.del_queue(get_game)
            await message.message.answer(f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=message.from_user.id, amount=amount)
            await message.bot.send_message(get_game, f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=get_game, amount=amount)
    elif user.balance <= 24.9:
        await message.message.answer(f'У Вас не достаточно средств для игры, пополните баланс!\n'
                                     f'\n', parse_mode='html', reply_markup=faunds_menu)


@dp.callback_query_handler(text='50/1')
async def amount_game(message: types.CallbackQuery):
    amount = 50
    await message.message.delete()
    user = await quick_commands.select_user(message.from_user.id)
    if user.balance >= 50.0:
        get_game = await quick_commands.get_game(user_id=message.from_user.id, amount=amount)
        if get_game == False:
            await message.message.answer(f'Идет поиск игры ⌛\n'
                                            f'\n', parse_mode='html', reply_markup=search_menu)
            await quick_commands.add_queue(user_id=message.from_user.id, amount=amount)
        else:
            await quick_commands.get_history(user_id=message.from_user.id, amount=amount)
            await quick_commands.del_queue(message.from_user.id)
            await quick_commands.del_queue(get_game)
            await message.message.answer(f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=message.from_user.id, amount=amount)
            await message.bot.send_message(get_game, f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=get_game, amount=amount)
    elif user.balance <= 49.9:
        await message.message.answer(f'У Вас не достаточно средств для игры, пополните баланс!\n'
                                     f'\n', parse_mode='html', reply_markup=faunds_menu)

@dp.callback_query_handler(text='100/1')
async def amount_game(message: types.CallbackQuery):
    amount = 100
    await message.message.delete()
    user = await quick_commands.select_user(message.from_user.id)
    if user.balance >= 100.0:
        get_game = await quick_commands.get_game(user_id=message.from_user.id, amount=amount)
        if get_game == False:
            await message.message.answer(f'Идет поиск игры ⌛\n'
                                            f'\n', parse_mode='html', reply_markup=search_menu)
            await quick_commands.add_queue(user_id=message.from_user.id, amount=amount)
        else:
            await quick_commands.get_history(user_id=message.from_user.id, amount=amount)
            await quick_commands.del_queue(message.from_user.id)
            await quick_commands.del_queue(get_game)
            await message.message.answer(f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=message.from_user.id, amount=amount)
            await message.bot.send_message(get_game, f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=get_game, amount=amount)
    elif user.balance <= 99.9:
        await message.message.answer(f'У Вас не достаточно средств для игры, пополните баланс!\n'
                                     f'\n', parse_mode='html', reply_markup=faunds_menu)


@dp.callback_query_handler(text='250/1')
async def amount_game(message: types.CallbackQuery):
    amount = 250
    await message.message.delete()
    user = await quick_commands.select_user(message.from_user.id)
    if user.balance >= 250.0:
        get_game = await quick_commands.get_game(user_id=message.from_user.id, amount=amount)
        if get_game == False:
            await message.message.answer(f'Идет поиск игры ⌛\n'
                                            f'\n', parse_mode='html', reply_markup=search_menu)
            await quick_commands.add_queue(user_id=message.from_user.id, amount=amount)
        else:
            await quick_commands.get_history(user_id=message.from_user.id, amount=amount)
            await quick_commands.del_queue(message.from_user.id)
            await quick_commands.del_queue(get_game)
            await message.message.answer(f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=message.from_user.id, amount=amount)
            await message.bot.send_message(get_game, f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=get_game, amount=amount)
    elif user.balance <= 249.9:
        await message.message.answer(f'У Вас не достаточно средств для игры, пополните баланс!\n'
                                     f'\n', parse_mode='html', reply_markup=faunds_menu)

@dp.callback_query_handler(text='500/1')
async def amount_game(message: types.CallbackQuery):
    amount = 500
    await message.message.delete()
    user = await quick_commands.select_user(message.from_user.id)
    if user.balance >= 500.0:
        get_game = await quick_commands.get_game(user_id=message.from_user.id, amount=amount)
        if get_game == False:
            await message.message.answer(f'Идет поиск игры ⌛\n'
                                            f'\n', parse_mode='html', reply_markup=search_menu)
            await quick_commands.add_queue(user_id=message.from_user.id, amount=amount)
        else:
            await quick_commands.get_history(user_id=message.from_user.id, amount=amount)
            await quick_commands.del_queue(message.from_user.id)
            await quick_commands.del_queue(get_game)
            await message.message.answer(f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=message.from_user.id, amount=amount)
            await message.bot.send_message(get_game, f'Игра найдена!\n'
                                         f'\n', parse_mode='html', reply_markup=knb_menu)
            await quick_commands.game_balance(user_id=get_game, amount=amount)
    elif user.balance <= 499.9:
        await message.message.answer(f'У Вас не достаточно средств для игры, пополните баланс!\n'
                                     f'\n', parse_mode='html', reply_markup=faunds_menu)