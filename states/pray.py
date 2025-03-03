from aiogram.filters.state import StatesGroup, State


class PrayTypes(StatesGroup):
    types = State()
    videos = State()