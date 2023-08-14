from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⚙️ Аккаунт'),
            KeyboardButton(text='🔎 Поиск игры')
        ],
        [
            KeyboardButton(text='💸️ Промокод'),
        ],
        [
            KeyboardButton(text='🎁 Бонус')
        ]
    ],
    resize_keyboard=True
)

ac_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📥 Пополнить баланс'),
            KeyboardButton(text='📤 Вывод средств'),
            KeyboardButton(text='🔎 Поиск игры')
        ],
        [
            KeyboardButton(text='💸️ Промокод'),
            KeyboardButton(text='🎁 Бонус')
        ],
        [
            KeyboardButton(text='🤝 Реферальная программа')
        ]

    ], resize_keyboard=True
)
zad_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔄 Обновить'),
            KeyboardButton(text='⚙️ Аккаунт'),
            KeyboardButton(text='🤝 Реферальная программа')
        ]

    ], resize_keyboard=True
)
ref_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⚙️ Аккаунт')
        ]
    ], resize_keyboard=True
)

search_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='❌️ Остановить поиск'),
        ]
    ],     resize_keyboard=True
)




knb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗿 Камень'),
            KeyboardButton(text='✂️ Ножницы'),
            KeyboardButton(text='📝 Бумага')
        ],
        [
            # KeyboardButton(text='🎲 Рандом')
        ]
    ],     resize_keyboard=True
)

fin_game = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⚙️ Аккаунт'),
            KeyboardButton(text='🔎 Поиск игры'),
        ]
    ],    resize_keyboard=True
)

faunds_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📥 Пополнить баланс'),
            KeyboardButton(text='⚙️ Аккаунт'),
        ]
    ],     resize_keyboard=True
)

promo_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙 Назад'),]
    ], resize_keyboard=True
)

time_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⌛ ждем ход противника'),
        ]
    ], resize_keyboard=True
)

wndrbl_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📲 Создать заявку'),
            KeyboardButton(text='🔙 Вернуться')
        ]
    ], resize_keyboard=True
)

