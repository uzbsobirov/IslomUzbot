from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back')
        ]
    ]
)