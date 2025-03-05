from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards.inline.back import main_back

router = Router()


#######  ERKAKLAR UCHUN NAMOQ O'QISHNI O'RGANISH

@router.callback_query(F.data == "for_men")
async def men_pray_videos_type(call: types.CallbackQuery, state: FSMContext):
    video_list = [
        "https://t.me/islom_medias/10",
        "https://t.me/islom_medias/11",
        "https://t.me/islom_medias/12",
        "https://t.me/islom_medias/13",
        "https://t.me/islom_medias/14",
        "https://t.me/islom_medias/15"
    ]

    await call.message.delete()
    text = "<b>👳‍♂️Erkaklar uchun namoz o'qishni o'rganish👇👇👇</b>"
    await call.message.answer(text=text)
    for video in video_list:
        await call.message.answer_video(video=video)

    await call.message.answer(text="Asosiy menuga qaytish", reply_markup=main_back)


@router.callback_query(F.data == "for_women")
async def women_pray_videos_type(call: types.CallbackQuery, state: FSMContext):
    video_list = [
        "https://t.me/islom_medias/17",
        "https://t.me/islom_medias/18",
        "https://t.me/islom_medias/19",
        "https://t.me/islom_medias/20",
        "https://t.me/islom_medias/21"
    ]

    await call.message.delete()
    text = "<b>🧕🏻Ayollar uchun namoz o'qishni o'rganish👇👇👇</b>"
    await call.message.answer(text=text)
    for video in video_list:
        await call.message.answer_video(video=video)

    await call.message.answer(text="Asosiy menuga qaytish", reply_markup=main_back)





