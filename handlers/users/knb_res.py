from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import knb_menu, fin_game, time_menu
from utils.dbapi import quick_commands




@dp.message_handler(text='🗿 Камень')
async def command_start(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        protivnic = await quick_commands.select_game(user_id=message.from_user.id)
        amount = await quick_commands.select_amount(user_id=message.from_user.id)
        res_prot = await quick_commands.game_res(user_one= message.from_user.id, user_two=protivnic, user_one_res='Камень')
        await quick_commands.his_res(user_one= message.from_user.id, user_two=protivnic, user_one_res='Камень')
        if res_prot == '0':
            await message.answer('Ваш противник еще не сделал ход, ждем его', reply_markup=time_menu)
            await message.bot.send_message(protivnic, f'Ваш противник сделал ход, ожидаем только Вас')
        else:
            if res_prot == 'Камень':
                await quick_commands.draw(user_one=message.from_user.id, user_two=protivnic)
                await message.answer('😳 Ничья! Противник тоже выбрал Камень! Сыграйте еще раз против него 😉', reply_markup=knb_menu)
                await message.bot.send_message(protivnic, '😳 Ничья! Противник тоже выбрал Камень! Сыграйте еще раз против него 😉', reply_markup=knb_menu)
            if res_prot == 'Бумага':
                await quick_commands.winner_res(user_one=message.from_user.id, user_two=protivnic, winner=protivnic)
                await quick_commands.win_hest(user_one=message.from_user.id, user_two=protivnic, winner=protivnic)
                await message.answer('Вы проиграли 😒, бумага противника обернула Ваш камень', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=message.from_user.id)
                await quick_commands.upd_luss_game(user_id=message.from_user.id)
                await message.bot.send_message(protivnic, f'Вы победили 🏆, Ваша бумага обернула камень противника!\n'
                                     f'💰 Ваш выигрыш составил {((amount * 2) - (((amount * 2) * 20)/ 100))}₽\n'
                                     f'🥳 Поздравляем! 🎉', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=protivnic)
                await quick_commands.upd_win_game(user_id=protivnic)
                await quick_commands.gamewin_balance(user_id=protivnic, amount=amount)
                await quick_commands.del_game(user_one=message.from_user.id, user_two=protivnic)
            if res_prot == 'Ножницы':
                await quick_commands.winner_res(user_one=message.from_user.id, user_two=protivnic, winner=message.from_user.id)
                await quick_commands.win_hest(user_one=message.from_user.id, user_two=protivnic, winner=message.from_user.id)
                await message.answer(f'Вы победили 🏆, Ваш камень сломал ножницы противника!\n'
                                     f'💰 Ваш выигрыш составил {((amount * 2) - (((amount * 2) * 20)/ 100))}₽\n'
                                     f'🥳 Поздравляем! 🎉', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=message.from_user.id)
                await quick_commands.upd_win_game(user_id=message.from_user.id)
                await quick_commands.gamewin_balance(user_id=message.from_user.id, amount=amount)
                await message.bot.send_message(protivnic, 'Вы проиграли 😒, Ваши ножницы сломались об камень противника', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=protivnic)
                await quick_commands.upd_luss_game(user_id=protivnic)
                await quick_commands.del_game(user_one=message.from_user.id, user_two=protivnic)
    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')


@dp.message_handler(text='✂️ Ножницы')
async def command_start(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        amount = await quick_commands.select_amount(user_id=message.from_user.id)
        protivnic = await quick_commands.select_game(user_id=message.from_user.id)
        res_prot = await quick_commands.game_res(user_one= message.from_user.id, user_two=protivnic, user_one_res='Ножницы')
        await quick_commands.his_res(user_one=message.from_user.id, user_two=protivnic, user_one_res='Ножницы')
        if res_prot == '0':
            await message.answer('Ваш противник еще не сделал ход, ждем его', reply_markup=time_menu)
            await message.bot.send_message(protivnic, f'Ваш противник сделал ход, ожидаем только Вас')
        else:
            if res_prot == 'Ножницы':
                await quick_commands.draw(user_one=message.from_user.id, user_two=protivnic)
                await message.answer('😳 Ничья! Противник тоже выбрал Ножницы! Сыграйте еще раз против него 😉', reply_markup=knb_menu)
                await message.bot.send_message(protivnic, '😳 Ничья! Противник тоже выбрал Ножницы! Сыграйте еще раз против него 😉', reply_markup=knb_menu)
            if res_prot == 'Бумага':
                await quick_commands.winner_res(user_one=message.from_user.id, user_two=protivnic, winner=message.from_user.id)
                await quick_commands.win_hest(user_one=message.from_user.id, user_two=protivnic,winner=message.from_user.id)
                await message.answer(f'Вы победили 🏆, Ваши ножницы порезали бумагу противника!\n'
                                     f'💰 Ваш выигрыш составил {((amount * 2) - (((amount * 2) * 20)/ 100))}₽\n'
                                     f'🥳 Поздравляем! 🎉', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=message.from_user.id)
                await quick_commands.upd_win_game(user_id=message.from_user.id)
                await quick_commands.gamewin_balance(user_id=message.from_user.id, amount=amount)
                await message.bot.send_message(protivnic, 'Вы проиграли 😒, ножницы противника порезали Вашу бумагу!', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=protivnic)
                await quick_commands.upd_luss_game(user_id=protivnic)
                await quick_commands.del_game(user_one=message.from_user.id, user_two=protivnic)
            if res_prot == 'Камень':
                await quick_commands.winner_res(user_one=message.from_user.id, user_two=protivnic, winner=protivnic)
                await quick_commands.win_hest(user_one=message.from_user.id, user_two=protivnic,winner=protivnic)
                await message.answer('Вы проиграли 😒, Ваши ножницы сломались об камень противника!', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=message.from_user.id)
                await quick_commands.upd_luss_game(user_id=message.from_user.id)
                await message.bot.send_message(protivnic, f'Вы победили 🏆, Ваш камень сломал ножницы противника!\n'
                                     f'💰 Ваш выигрыш составил {((amount * 2) - (((amount * 2) * 20)/ 100))}₽\n'
                                     f'🥳 Поздравляем! 🎉', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=protivnic)
                await quick_commands.upd_win_game(user_id=protivnic)
                await quick_commands.gamewin_balance(user_id=protivnic, amount=amount)
                await quick_commands.del_game(user_one=message.from_user.id, user_two=protivnic)
    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')

@dp.message_handler(text='📝 Бумага')
async def command_start(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    if user.status == 'active':
        amount = await quick_commands.select_amount(user_id=message.from_user.id)
        protivnic = await quick_commands.select_game(user_id=message.from_user.id)
        res_prot = await quick_commands.game_res(user_one= message.from_user.id, user_two=protivnic, user_one_res='Бумага')
        await quick_commands.his_res(user_one=message.from_user.id, user_two=protivnic, user_one_res='Бумага')
        if res_prot == '0':
            await message.answer('Ваш противник еще не сделал ход, ждем его', reply_markup=time_menu)
            await message.bot.send_message(protivnic, f'Ваш противник сделал ход, ожидаем только Вас')
        else:
            if res_prot == 'Бумага':
                await quick_commands.draw(user_one=message.from_user.id, user_two=protivnic)
                await message.answer('😳 Ничья! Противник тоже выбрал Бумага! Сыграйте еще раз против него 😉', reply_markup=knb_menu)
                await message.bot.send_message(protivnic, '😳 Ничья! Противник тоже выбрал Бумага! Сыграйте еще раз против него 😉', reply_markup=knb_menu)
            if res_prot == 'Ножницы':
                await quick_commands.winner_res(user_one=message.from_user.id, user_two=protivnic, winner=protivnic)
                await quick_commands.win_hest(user_one=message.from_user.id, user_two=protivnic,winner=protivnic)
                await message.answer('Вы проиграли 😒, ножницы противника порезали Вашу бумагу!', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=message.from_user.id)
                await quick_commands.upd_luss_game(user_id=message.from_user.id)
                await message.bot.send_message(protivnic, f'Вы победили 🏆, Ваши ножницы порезали бумагу противника!\n'
                                     f'💰 Ваш выигрыш составил {((amount * 2) - (((amount * 2) * 20)/ 100))}₽\n'
                                     f'🥳 Поздравляем! 🎉', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=protivnic)
                await quick_commands.upd_win_game(user_id=protivnic)
                await quick_commands.gamewin_balance(user_id=protivnic, amount=amount)
                await quick_commands.del_game(user_one=message.from_user.id, user_two=protivnic)
            if res_prot == 'Камень':
                await quick_commands.winner_res(user_one=message.from_user.id, user_two=protivnic, winner=message.from_user.id)
                await quick_commands.win_hest(user_one=message.from_user.id, user_two=protivnic,winner=message.from_user.id)
                await message.answer(f'Вы победили 🏆, Ваша бумага обернула камень противника!\n'
                                     f'💰 Ваш выигрыш составил {((amount * 2) - (((amount * 2) * 20)/ 100))}₽\n'
                                     f'🥳 Поздравляем! 🎉', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=message.from_user.id)
                await quick_commands.upd_win_game(user_id=message.from_user.id)
                await quick_commands.gamewin_balance(user_id=message.from_user.id, amount=amount)
                await message.bot.send_message(protivnic, 'Вы проиграли😒, бумага противника обернула Ваш камень!', reply_markup=fin_game)
                await quick_commands.upd_all_game(user_id=protivnic)
                await quick_commands.upd_luss_game(user_id=protivnic)
                await quick_commands.del_game(user_one=message.from_user.id, user_two=protivnic)
    if user.status == 'ban':
        await message.answer('Вы заблокированы за махинации')


@dp.message_handler(text='⌛ ждем ход противника')
async def whait(message: types.Message):
    await message.delete()
    await message.answer('Все еще ждем хода вашего противника')
