from aiogram import Router, types, F
from aiogram.filters.command import Command
import logging
from keyboards import keyboard
from random_fox import fox

router = Router()

@router.message(F.text)
async def msg(message: types.Message):
    if 'добрый день!' in message.text.lower():
        await message.reply('И тебе добрый день!)')
    elif 'как дела?' in message.text.lower():
        await message.reply('Отлично, а у тебя?)')
    else:
        await message.reply('Извини, я тебя не понял(...')
