import requests


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

print(get_pray_time("Farg'ona"))