from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import kb_menu
from utils.misc import rate_limit
from utils.dbapi import quick_commands
from aiogram.dispatcher.filters import CommandStart


@rate_limit(limit=15)

@dp.message_handler(CommandStart())
async def command_start(message: types.Message):
    args = message.get_args()
    new_args = await quick_commands.check_args(args, message.from_user.id)
    try:
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'<strong>Добро пожаловать в наш бот по игре "🗿 Камень, ✂️ ножницы, 📝 бумага"!</strong>\n'
                                 f'Правила игры можно посмотреть через команду /rules\n'
                                 f' · Вы можете получить бонус 25₽ нажав на кнопку "🎁 Бонус"\n'
                                 f' · А так же активировать промокод(если он у вас есть) и получить бонусный баланс!\n'
                                 f' · Для старта игры вам нужно нажать на кнопку "🔎 Поиск игры"', parse_mode='html', reply_markup=kb_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы за махинации')
    except Exception:
        await quick_commands.add_user(user_id=message.from_user.id,
                                      f_name=message.from_user.first_name,
                                      l_name=message.from_user.last_name,
                                      referral_id=int(new_args),
                                      username=message.from_user.username,
                                      status= 'active',
                                      balance=0,
                                      all_game=0,
                                      win_game=0,
                                      luss_game=0,
                                      bonus_actie=0)
        await message.answer(f'<strong>Добро пожаловать в наш бот по игре "🗿 Камень, ✂️ ножницы, 📝 бумага"!</strong>\n'
                                 f'Правила игры можно посмотреть через команду /rules\n'
                                 f' · Вы можете получить бонус 25₽ нажав на кнопку "🎁 Бонус"\n'
                                 f' · А так же активировать промокод(если он у вас есть) и получить бонусный баланс!\n'
                                 f' · Для старта игры вам нужно нажать на кнопку "🔎 Поиск игры"', parse_mode='html', reply_markup=kb_menu)