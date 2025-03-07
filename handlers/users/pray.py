from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from keyboards.inline.back import main_back, back
from keyboards.inline.main import main
from keyboards.inline.pray_buttons import pray_text
from states.pray import Ramadan

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


######### IFTAR and SUHOOR ########

@router.callback_query(F.data == "ramadan_section")
async def ramadan_section(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    photo = "https://t.me/islom_medias/22"
    caption = "<b>Kerakli bo'limni tanlang👇👇👇</b>"
    await call.message.answer_photo(photo=photo, caption=caption, reply_markup=pray_text)
    await state.set_state(Ramadan.types)


@router.callback_query(Ramadan.types)
async def get_section(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    await state.update_data(type=data)
    await state.set_state(Ramadan.type)


@router.callback_query(Ramadan.type)
async def section(call: types.CallbackQuery, state: FSMContext):
    full_name = call.message.from_user.full_name
    user_mention = call.message.from_user.mention_html(full_name)
    data = await state.get_data()
    type = data.get("type")
    print(await state.get_state())
    await call.message.delete()

    if type == "ogiz_ochish":
        photo1 = "https://t.me/islom_medias/7"
        caption = """<b>Ифторлик (оғиз очиш) дуоси ✨

    Аллоҳумма лака сумту ва бика ааманту ва аълайка таваккалту ва аълаа ризқика афтарту,
    фағфирлий ма қоддамту ва маа аххорту бироҳматика йаа арҳамар рооҳимийн.

    Маъноси: Эй Аллоҳ, ушбу Рўзамни Сен учун тутдим ва Сенга иймон келтирдим ва Сенга таваккал қилдим ва берган ризқинг
    билан ифтор қилдим. Эй меҳрибонларнинг энг меҳрибони, менинг аввалги ва кейинги гуноҳларимни мағфират қилгил.</b>"""
        await call.message.answer_photo(photo=photo1, caption=caption, reply_markup=back)

    elif type == "ogiz_yopish":
        photo2 = "https://t.me/islom_medias/8"
        caption = "<b>Рўза тутиш (саҳарлик, оғиз ёпиш) дуоси ✨\n\n" \
                  "Навайту ан асувма совма шаҳри рамазона минал фажри илал мағриби, " \
                  "холисан лиллаҳи таъаалаа Аллоҳу акбар.\n\nМаъноси: Рамазон ойининг " \
                  "рўзасини субҳдан то кун ботгунча тутмоқни ният қилдим. Холис Аллоҳ учун Аллоҳ буюкдир.</b>"
        await call.message.answer_photo(photo=photo2, caption=caption, reply_markup=back)

    else:
        main_photo = "https://t.me/islom_medias/9"
        start_text = f"""<b>Assalomu aleykum {user_mention}❗️
            Sizni botimizda ko'rib turganimizdan xursandmiz😊
            Sizga kerakli bo'lgan bo'limni tanlang👇</b>"""
        await call.message.answer_photo(caption=start_text, parse_mode=ParseMode.HTML,
                                        photo=main_photo, reply_markup=main)
        await state.clear()
    await state.clear()





