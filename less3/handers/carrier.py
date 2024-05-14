from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def nake_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    keyword = ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
    return keyword