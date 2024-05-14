from random import random

from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
import logging

from aiogram.fsm.state import StatesGroup, State
from keyboards.carrier_keybort import nake_keybord


router = Router()


available_jobs = [
    'Программист'
    'Маркетолог'
    'Аналитик'
    'Менеджер'
    'Дизайнер'
]
available_grades = [
    'Низкий'
    'Средний'
    'Высокий'
]

class Choice(StatesGroup):
    job = State()
    grade = State()

    @router.message(Command(commands=['prof']))
    async def prof(self, message: types.Message, state: FSMContext):
        await message.answer('Какая профессия вас интересует?', reply_markup=nake_keybord(available_jobs))
        await state.set_state(Choice.job)

@router.message(Choice.job, F.text.in_(available_jobs))
async def jobs(message: types.Message, state: FSMContext):
    await message.answer('Как вы оцениваете свою профессию?', reply_markup=nake_keybord(available_jobs, available_grades))
    await state.set_state(Choice.job, grade)

@router.message(Choice.job):
    async def job_incorrectly(message: types.Message):
        await message.answer('Неправильно. Попробуй еще раз', reply_markup=nake_keybord(available_jobs))

@router.message(Choice.grade, F.text.in_(available_grades))
async def grade(message: types.Message, state: FSMContext):
    await message.answer(f'Вы все прошли, с вами свяжутся наши hr{message.text}', reply_markup=types.ReplyKeyboardRemove)
    await state.claer()


@router.message(Choice.grade):
    async def grade_incorrectly(message: types.Message):
        await message.answer('Неправильно. Попробуй еще раз', reply_markup=nake_keybord(available_grades))
