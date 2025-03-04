from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from aiogram.fsm.context import FSMContext

from loader import db, bot
from data.config import ADMINS
from states import PrayTypes
from utils.extra_datas import make_title
from keyboards.inline.main import main

router = Router()


@router.callback_query(PrayTypes.types, F.data == "back")
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    full_name = call.message.from_user.full_name
    user_mention = call.message.from_user.mention_html(full_name)

    await call.message.delete()
    main_photo = "https://t.me/islom_medias/9"
    start_text = f"""<b>Assalomu aleykum {user_mention}❗️
    Sizni botimizda ko'rib turganimizdan xursandmiz😊
    Sizga kerakli bo'lgan bo'limni tanlang👇</b>"""
    await call.message.answer_photo(caption=start_text, parse_mode=ParseMode.HTML,
                                    photo=main_photo, reply_markup=main)
    await state.clear()
