import json
import codecs
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from keyboards.inline.back import main_back
from states.pray import Quran

router = Router()

with codecs.open('verses.json', 'r', encoding='utf-8', errors='ignore') as file:
    verses = json.load(file)
    quran = verses['quran']


@router.callback_query(F.data == "quran_book")
async def give_quran(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Sizga nechanchi bob kerak? Sonlarda kiriting👇👇👇</b>")
    await state.set_state(Quran.chapter)


@router.message(Quran.chapter)
async def get_chapter(message: types.Message, state: FSMContext):
    chapter = message.text
    if chapter.isdigit():
        if int(chapter) <= 114:
            await message.answer(f"<b>{chapter}-bobning nechanchi oyati kerak?👇👇👇</b>")
            await state.update_data(chapter=chapter)
            await state.set_state(Quran.verse)
        else:
            await message.answer(text="Bunday ma'lumot topilmadi, qaytadan urinib ko'ring")
            await state.set_state(Quran.chapter)
    else:
        await message.answer(text="<b>Iltimos faqat sonlardan foydalaning, boshqattan kiriting</b>")
        await state.set_state(Quran.chapter)


@router.message(Quran.verse)
async def geet_verse(message: types.Message, state: FSMContext):
    verse = message.text
    data = await state.get_data()
    chapter = data.get("chapter")
    if verse.isdigit():
        for what in quran:
            if int(chapter) == what['chapter']:
                if int(verse) == what['verse']:
                    await message.answer(text=what['text'], reply_markup=main_back)
                    await state.clear()
                    break
    else:
        await message.answer(text="<b>Iltimos faqat sonlardan foydalaning, boshqattan kiriting</b>")
        await state.set_state(Quran.verse)