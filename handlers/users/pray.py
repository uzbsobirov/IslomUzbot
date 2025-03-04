from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from aiogram.fsm.context import FSMContext

from keyboards.inline.pray import pray
from loader import db, bot
from data.config import ADMINS
from states import PrayTypes
from utils.extra_datas import make_title
from keyboards.inline.main import main

router = Router()


@router.callback_query(F.data == "for_men")
async def men_pray_videos_type(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>👳‍♂️Erkaklar uchun namoz o'qishni o'rganish👇👇👇</b>"
    await call.message.answer(text=text, reply_markup=pray)
    await state.set_state(PrayTypes.types)


@router.callback_query(PrayTypes.types)
async def men_pray_videos(call: types.CallbackQuery, state: FSMContext):
    # video_list = [
    #     "https://t.me/islom_medias/10",
    #     "https://t.me/islom_medias/11",
    #     "https://t.me/islom_medias/12",
    #     "https://t.me/islom_medias/13",
    #     "https://t.me/islom_medias/14",
    #     "https://t.me/islom_medias/15"
    # ]
    #
    data = call.data
    await state.update_data(type_pray=data)
    await state.set_state(PrayTypes.videos)

@router.callback_query(PrayTypes.videos)
async def men_pray_videos(call: types.CallbackQuery, state: FSMContext):
    print(call.data)
    get_state_data = await state.get_data()
    data = get_state_data.get("type_pray")
    print(data)



