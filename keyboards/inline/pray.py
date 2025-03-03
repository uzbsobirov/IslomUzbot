from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

pray = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bomdod", callback_data='bomdod'),
            InlineKeyboardButton(text="Peshin", callback_data='peshin')
        ],
        [
            InlineKeyboardButton(text="Asr", callback_data='asr'),
            InlineKeyboardButton(text="Shom", callback_data='shom')
        ],
        [
            InlineKeyboardButton(text="Xufton", callback_data='xufton'),
            InlineKeyboardButton(text="Janoza namozi", callback_data='janoza')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back')
        ]
    ]
)