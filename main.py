import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import keyboard
from random_fox import fox

#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: types.Message):
     await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)

@dp.message(Command(commands=['число']))
@dp.message(F.text.lower()== 'число')
async def info(message: types.Message):
    number = random.randint(1,100)
    await message.answer(f'Итак,  твое число: {number}!')


@dp.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.anweser('Привет, лови лису!')
    await message.answer_photo(img_fox)
    await bot.send_photo(message.from_user.id, img_fox)

@dp.message(Command(commands=['stop']))
async def stop(message: types.Message):
       await message.answer(f'До скорых встреч, {message.from_user.full_name}!')

@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("Я бот - твой друг и товарищ ;) ")

@dp.message(F.text)
async def msg(message: types.Message):
    if 'добрый день!' in message.text.lower():
        await message.reply('И тебе добрый день!)')
    elif 'как дела?' in message.text.lower():
        await message.reply('Отлично, а у тебя?)')
    else:
        await message.reply('Извини, я тебя не понял(...')

async def main():
   await dp.start_polling(bot)


if __name__ == '__main__':
   asyncio.run(main())