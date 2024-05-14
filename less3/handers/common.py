
from aiogram import Router, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import keyboard
from random_fox import fox

router = Router()

@router.message(Command(commands=['start']))
async def start(message: types.Message):
     await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)

@router.message(Command(commands=['число']))
@router.message(F.text.lower()== 'число')
async def info(message: types.Message):
    number = random.randint(1,100)
    await message.answer(f'Итак,  твое число: {number}!')

@router.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.anweser('Привет, лови лису!')
    await message.answer_photo(img_fox)
    await bot.send_photo(message.from_user.id, img_fox)

@router.message(Command(commands=['stop']))
    async def stop(message: types.Message):
        await message.answer(f'До скорых встреч, {message.from_user.full_name}!')

@router.message(Command("info"))
    async def cmd_info(message: types.Message):
        await message.reply("Я бот - твой друг и товарищ ;) ")