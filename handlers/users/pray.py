from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards.inline.back import back
from keyboards.inline.pray import pray
from states.pray import PrayTypes
from keyboards.inline.main import main
from aiogram.enums.parse_mode import ParseMode
from loader import bot

router = Router()


@router.callback_query(F.data == 'for_men')
async def for_men_pray(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(call_data=call.data)
    await call.message.delete()
    await call.message.answer(text="👳<b>‍♂️Erkaklar uchun namoz o'qishni o'rganish👇👇👇</b>",
                              reply_markup=pray)
    await state.set_state(PrayTypes.types)


@router.callback_query(PrayTypes.types)
async def pray_types(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    men_ideos = [
        "https://t.me/islom_medias/10",
        "https://t.me/islom_medias/11",
        "https://t.me/islom_medias/12",
        "https://t.me/islom_medias/13",
        "https://t.me/islom_medias/14",
        "https://t.me/islom_medias/15"
    ]

    await call.message.delete()
    if data == "bomdod":
        await call.message.answer_video(caption="<b>Erkaklar uchun bomdod namozi</b>", video=men_ideos[0],
                                        reply_markup=back)
        await state.set_state(PrayTypes.videos)
    elif data == "peshin":
        await call.message.answer_video(caption="<b>Erkaklar uchun peshin namozi</b>", video=men_ideos[1],
                                        reply_markup=back)
        await state.set_state(PrayTypes.videos)
    elif data == "asr":
        await call.message.answer_video(caption="<b>Erkaklar uchun asr namozi</b>", video=men_ideos[2],
                                        reply_markup=back)
        await state.set_state(PrayTypes.videos)
    elif data == "shom":
        await call.message.answer_video(caption="<b>Erkaklar uchun shom namozi</b>", video=men_ideos[3],
                                        reply_markup=back)
        await state.set_state(PrayTypes.videos)
    elif data == "xufton":
        await call.message.answer_video(caption="<b>Erkaklar uchun xufton namozi</b>", video=men_ideos[4],
                                        reply_markup=back)
        await state.set_state(PrayTypes.videos)
    elif data == "janoza":
        await call.message.answer_video(caption="<b>Erkaklar uchun janoza namozi</b>", video=men_ideos[5],
                                        reply_markup=back)
        await state.set_state(PrayTypes.videos)


##### "ORQAGA" tugmasi uchun funksiyalar #####

@router.callback_query(PrayTypes.videos, F.data == "back")
async def back_to_pray_types(call: types.CallbackQuery, state: FSMContext):
    print(2)
    data = await state.get_data()
    new_data = data.get("call_data")
    if new_data == "for_men":
        await call.message.delete()
        await call.message.answer(text="👳<b>‍♂️Erkaklar uchun namoz o'qishni o'rganish👇👇👇</b>",
                                  reply_markup=pray)
        await state.set_state(PrayTypes.types)
    else:
        pass


@router.callback_query(PrayTypes.types, F.data == "back")
async def back_to_pray_types(call: types.CallbackQuery, state: FSMContext):
    full_name = call.message.from_user.full_name
    user_mention = call.message.from_user.mention_html(full_name)
    print(1)

    # await call.message.delete()
    main_photo = "https://t.me/islom_medias/9"
    start_text = f"""<b>Assalomu aleykum {user_mention}❗️
    Sizni botimizda ko'rib turganimizdan xursandmiz😊
    Sizga kerakli bo'lgan bo'limni tanlang👇</b>"""
    await call.message.answer_photo(caption=start_text, parse_mode=ParseMode.HTML,
                               photo=main_photo, reply_markup=main)
    await state.clear()

