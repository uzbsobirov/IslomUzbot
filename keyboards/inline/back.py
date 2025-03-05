from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='main_back')
        ]
    ]
)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back')
        ]
    ]
)