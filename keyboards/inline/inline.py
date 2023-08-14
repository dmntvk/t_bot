from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('🗿 Камень, ✂️ ножницы, 📝 бумага', callback_data='https://t.me/+eGt8qTWkH_E0YTVi'),
        InlineKeyboardButton('🎲 Кубик',callback_data='asd'),
        InlineKeyboardButton('🎯 Дартс', callback_data='sad'),
    ]
])

bns_menu = InlineKeyboardMarkup(inline_keyboard=
                                [
                                    [
                                        InlineKeyboardButton('Подписаться!', url='https://t.me/justttdoitbot')
                                    ],
                                    [
                                        InlineKeyboardButton('Проверить подписку!', callback_data='checks_sub')
                                    ]
                                ])

game_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('🗿 Камень, ✂️ ножницы, 📝 бумага', callback_data='🗿 Камень, ✂️ ножницы, 📝 бумага'),
    ],
    [
    ]
])

kbm_amount_menu = InlineKeyboardMarkup(inline_keyboard=
                                   [
                                       [
                                           InlineKeyboardButton('10₽', callback_data='10/1'),
                                           InlineKeyboardButton('25₽', callback_data='25/1'),
                                           InlineKeyboardButton('50₽', callback_data='50/1'),
                                       ],
                                       [
                                           InlineKeyboardButton('100₽', callback_data='100/1'),
                                           InlineKeyboardButton('250₽', callback_data='250/1'),
                                           InlineKeyboardButton('500₽', callback_data='500/1'),
                                       ]
                                   ]
)

b_up_menu = InlineKeyboardMarkup(inline_keyboard=
                                 [
                                     [
                                    InlineKeyboardButton('10₽', callback_data='10'),
                                     InlineKeyboardButton('25₽', callback_data='25'),
                                     InlineKeyboardButton('50₽', callback_data='50'),
                                     ],
                                        [
                                           InlineKeyboardButton('100₽', callback_data='100'),
                                           InlineKeyboardButton('250₽', callback_data='250'),
                                           InlineKeyboardButton('500₽', callback_data='500'),
                                       ]
                                 ]
)

def oplata(isUrl=True, url='', bill=''):
    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if isUrl:
        oplata_link = InlineKeyboardButton(text='Оплатить', url=url)
        qiwiMenu.insert(oplata_link)
    btncheckQiwi = InlineKeyboardButton(text='Проверить оплату', callback_data='check_'+bill)
    qiwiMenu.insert(btncheckQiwi)
    cancel = InlineKeyboardButton(text='Отменить оплату', callback_data='cancel'+bill)
    qiwiMenu.insert(cancel)
    return qiwiMenu

create_w_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('🥝 Qiwi', callback_data='qiwi')
    ]
])