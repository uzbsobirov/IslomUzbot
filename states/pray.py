from aiogram.filters.state import StatesGroup, State


class PrayTime(StatesGroup):
    region = State()


class Quran(StatesGroup):
    chapter = State()
    verse = State()


class Ramadan(StatesGroup):
    types = State()
    type = State()