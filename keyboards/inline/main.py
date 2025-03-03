from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👳‍♂️Erkaklar uchun", callback_data='for_men'),
            InlineKeyboardButton(text="🧕🏻Ayollar uchun", callback_data='for_women')
        ],
        [
            InlineKeyboardButton(text="🕔Namoz vaqtlari", callback_data='pray_time'),
            InlineKeyboardButton(text="📖Quran", callback_data='quran_book')
        ],
        [
            InlineKeyboardButton(text="🌙Ramazon bo'limi", callback_data='ramadan_section')
        ],
        [
            InlineKeyboardButton(text="📨Fikr bildirish", callback_data='comment')
        ]
    ]
)


inline_keyboard = [[
    InlineKeyboardButton(text="✅ Yes", callback_data='yes'),
    InlineKeyboardButton(text="❌ No", callback_data='no')
]]
are_you_sure_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
