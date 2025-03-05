from uu import Error

from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
import requests

from keyboards.inline.pray_buttons import pray_region
from states import PrayTime
from keyboards.inline.back import back

router = Router()


def get_pray_time(region):
    url = f"https://islomapi.uz/api/present/day?region={region}"
    response = requests.get(url).json()
    region = response['region']
    date = response['date']
    weekday = response['weekday']
    text = f"\n\n<b><i>📆 Bugunki sana</i></b>: <b>{date}</b>\n<b><i>〽️ " \
           f"Bugunki kun</i></b>: <b>{weekday}</b>\n<i><b>🏢 " \
           f"Shaxar</b></i> - <b>( {region} )</b>\n\n<b><i>🌇 " \
           f"Tong saharlik</i></b> - <b>{response['times']['tong_saharlik']}</b>\n\n<b><i>🌅 " \
           f"Quyosh</i></b> - <b>{response['times']['quyosh']}</b>\n\n<b><i>🏞 " \
           f"Peshin</i></b> - <b>{response['times']['peshin']}</b>\n\n<b><i>🌇 " \
           f"Asr</i></b> - <b>{response['times']['asr']}</b>\n\n<b><i>🌄 " \
           f"Shom</i></b> - <b>{response['times']['shom_iftor']}</b>\n\n<b><i>🌃 " \
           f"Hufton</i></b> - <b>{response['times']['hufton']}</b>\n\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\nوَٱللَّهُ يُرِيد" \
           f"ُ أَن يَتُوبَ عَلَيۡكُمۡ وَيُرِيد" \
           f"ُ ٱلَّذِينَ يَتَّبِعُونَ ٱلشَّهَوَٰتِ" \
           f" أَن تَمِيلُواْ مَيۡلًا عَظِيمٗا" \
           f"\n\nАlloh sizning tavbangizni qabul qilishni xohlaydir. Shahvatlarga ergashadiganlar esa, " \
           f"ulkan ogʼishga " \
           f"moyil boʼlishingizni xohlaydir.\n\n▫️Niso Surasi 27-oyat\n\n"

    return text


@router.callback_query(F.data == "pray_time")
async def give_pray_time(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="<b>Qaysi viloyat kerak ekanligini tanlang👇👇👇</b>", reply_markup=pray_region)
    await state.set_state(PrayTime.region)


@router.callback_query(PrayTime.region)
async def get_region(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    get_data = get_pray_time(region=call.data)
    try:
        await call.message.answer(get_data, reply_markup=back)
    except Exception as err:
        print(err)
        await call.message.answer("Xatolik yuz berdi, boshqatta unirib ko'ring", reply_markup=pray_region)