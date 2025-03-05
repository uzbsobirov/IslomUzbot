from aiogram.filters.state import StatesGroup, State


class PrayTime(StatesGroup):
    region = State()