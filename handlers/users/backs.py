from aiogram import Router, types, F
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext

from keyboards.inline.main import main
from keyboards.inline.pray_buttons import pray_region, pray_text
from states import PrayTime, Ramadan

router = Router()


@router.callback_query(F.data == "main_back")
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


@router.callback_query(PrayTime.region, F.data == "back")
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="<b>Qaysi viloyat kerak ekanligini tanlang👇👇👇</b>", reply_markup=pray_region)
    await state.set_state(PrayTime.region)


@router.callback_query(Ramadan.type, F.data == "back")
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    photo = "https://t.me/islom_medias/22"
    caption = "<b>Kerakli bo'limni tanlang👇👇👇</b>"
    await call.message.answer_photo(photo=photo, caption=caption, reply_markup=pray_text)
    await state.set_state(Ramadan.types)
