from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


pray_region = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Jizzax", callback_data='Jizzax'),
            InlineKeyboardButton(text="Buxoro", callback_data='Buxoro')
        ],
        [
            InlineKeyboardButton(text="Toshkent", callback_data='Toshkent'),
            InlineKeyboardButton(text="Navoiy", callback_data='Navoiy')
        ],
        [
            InlineKeyboardButton(text="Andijon", callback_data='Andijon'),
            InlineKeyboardButton(text="Namangan", callback_data='Namangan')
        ],
        [
            InlineKeyboardButton(text="Samarqand", callback_data='Urgut'),
            InlineKeyboardButton(text="Nukus", callback_data='Nukus')
        ],
        [
            InlineKeyboardButton(text="Farg'оna", callback_data="Farg'ona"),
            InlineKeyboardButton(text="Urganch", callback_data='Urganch')
        ],
        [
            InlineKeyboardButton(text="Termiz", callback_data='Termiz'),
            InlineKeyboardButton(text="Guliston", callback_data='Guliston')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='main_back')
        ]
    ]
)


pray_text = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✨ Ogiz ochish duosi", callback_data='ogiz_ochish'),
            InlineKeyboardButton(text="✨ Ogiz yopish duosi", callback_data='ogiz_yopish')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='main_back')
        ]
    ]
)
