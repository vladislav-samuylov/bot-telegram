import random

from aiogram.dispatcher.filters import Text
from config import TOKEN
from word_list import word_list
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

test = KeyboardButton('🇷🇺Начать тест (Start test)🇬🇧')
cancel = KeyboardButton('Отмена')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(test)
kb_cancel.add(cancel)

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer(f'В программе всего слов: {len(word_list)}', reply_markup=kb_client)

class FSMTest(StatesGroup):
    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()
    question_6 = State()
    question_7 = State()
    question_8 = State()
    question_9 = State()
    question_10 = State()

@dp.message_handler(lambda message: '🇷🇺Начать тест (Start test)🇬🇧' in message.text, state=None)
async def cm_start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['random_start'] = random.sample(range(len(word_list)), 10)
        data['right'] = 0
        data['wrong'] = 0
    await FSMTest.question_1.set()
    await message.answer(f"Переведи слово: {word_list[data['random_start'][0]][1]}", reply_markup=kb_cancel)

@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals='Отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Тест завершен', reply_markup=ReplyKeyboardRemove())
    await message.answer('Начать тест 👇👇👇', reply_markup=kb_client)

@dp.message_handler(state=FSMTest.question_1)
async def load_question_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = (word_list[data['random_start'][0]][0])
    async with state.proxy() as data:
        if answer == message.text:
            data['right'] += 1
            await message.reply('Правильный ответ 🎉🎉🎉')
        else:
            data['wrong'] += 1
            await message.reply(f"Не верно ❌❌❌, правильный ответ: {word_list[data['random_start'][0]][0]}")
    await message.answer(f"Переведи слово: {word_list[data['random_start'][1]][1]}")
    await FSMTest.next()

@dp.message_handler(state=FSMTest.question_2)
async def load_question_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = (word_list[data['random_start'][1]][0])
    async with state.proxy() as data:
        if answer == message.text:
            data['right'] += 1
            await message.reply('Правильный ответ 🎉🎉🎉')
        else:
            data['wrong'] += 1
            await message.reply(f"Не верно ❌❌❌, правильный ответ: {word_list[data['random_start'][1]][0]}")
    await message.answer(f"Переведи слово: {word_list[data['random_start'][2]][1]}")
    await FSMTest.next()

@dp.message_handler(state=FSMTest.question_3)
async def load_question_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = (word_list[data['random_start'][2]][0])
    async with state.proxy() as data:
        if answer == message.text:
            data['right'] += 1
            await message.reply('Правильный ответ 🎉🎉🎉')
        else:
            data['wrong'] += 1
            await message.reply(f"Не верно ❌❌❌, правильный ответ: {word_list[data['random_start'][2]][0]}")
    await message.answer(f"Переведи слово: {word_list[data['random_start'][3]][1]}")
    await FSMTest.next()

@dp.message_handler(state=FSMTest.question_4)
async def load_question_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = (word_list[data['random_start'][3]][0])
    async with state.proxy() as data:
        if answer == message.text:
            data['right'] += 1
            await message.reply('Правильный ответ 🎉🎉🎉')
        else:
            data['wrong'] += 1
            await message.reply(f"Не верно ❌❌❌, правильный ответ: {word_list[data['random_start'][3]][0]}")
    await message.answer(f"Переведи слово: {word_list[data['random_start'][4]][1]}")
    await FSMTest.next()

@dp.message_handler(state=FSMTest.question_5)
async def load_question_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = (word_list[data['random_start'][4]][0])
    async with state.proxy() as data:
        if answer == message.text:
            data['right'] += 1
            await message.reply('Правильный ответ 🎉🎉🎉')
        else:
            data['wrong'] += 1
            await message.reply(f"Не верно ❌❌❌, правильный ответ: {word_list[data['random_start'][4]][0]}")
    await message.answer(f"Переведи слово: {word_list[data['random_start'][5]][1]}")
    await FSMTest.next()

@dp.message_handler(state=FSMTest.question_6)
async def load_question_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = (word_list[data['random_start'][5]][0])
    async with state.proxy() as data:
        if answer == message.text:
            data['right'] += 1
            await message.reply('Правильный ответ 🎉🎉🎉')
        else:
            data['wrong'] += 1
            await message.reply(f"Не верно ❌❌❌, правильный ответ: {word_list[data['random_start'][5]][0]}")
    await message.answer(f"Переведи слово: {word_list[data['random_start'][6]][1]}")
    await FSMTest.next()

@dp.message_handler(state=FSMTest.question_7)
async def load_question_7(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = (word_list[data['random_start'][6]][0])
    async with state.proxy() as data:
        if answer == message.text:
            data['right'] += 1
            await message.reply('Правильный ответ 🎉🎉🎉')
        else:
            data['wrong'] += 1
            await message.reply(f"Не верно ❌❌❌, правильный ответ: {word_list[data['random_start'][6]][0]}")
    await message.answer(f"Переведи слово: {word_list[data['random_start'][7]][1]}")
    await FSMTest.next()

@dp.message_handler(state=FSMTest.question_8)
async def load_question_8(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = (word_list[data['random_start'][7]][0])
    async with state.proxy() as data:
        if answer == message.text:
            data['right'] += 1
            await message.reply('Правильный ответ 🎉🎉🎉')
        else:
            data['wrong'] += 1
            await message.reply(f"Не верно ❌❌❌, правильный ответ: {word_list[data['random_start'][7]][0]}")
    await message.answer(f"Переведи слово: {word_list[data['random_start'][8]][1]}")
    await FSMTest.next()

@dp.message_handler(state=FSMTest.question_9)
async def load_question_9(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = (word_list[data['random_start'][8]][0])
    async with state.proxy() as data:
        if answer == message.text:
            data['right'] += 1
            await message.reply('Правильный ответ 🎉🎉🎉')
        else:
            data['wrong'] += 1
            await message.reply(f"Не верно ❌❌❌, правильный ответ: {word_list[data['random_start'][8]][0]}")
    await message.answer(f"Переведи слово: {word_list[data['random_start'][9]][1]}")
    await FSMTest.next()

@dp.message_handler(state=FSMTest.question_10)
async def load_question_10(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = (word_list[data['random_start'][9]][0])
    async with state.proxy() as data:
        if answer == message.text:
            data['right'] += 1
            await message.reply('Правильный ответ 🎉🎉🎉')
        else:
            data['wrong'] += 1
            await message.reply(f"Не верно ❌❌❌, правильный ответ: {word_list[data['random_start'][9]][0]}")
    await message.answer(f"Правильных ответов: {data['right']}, Неправильных ответов: {data['wrong']}", reply_markup=ReplyKeyboardRemove())
    await message.answer('Начать тест 👇👇👇', reply_markup=kb_client)
    await state.finish()


executor.start_polling(dp, skip_updates=True)