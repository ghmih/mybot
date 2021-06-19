import logging
import os
import balaboba
import keyboard
from states import States

import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import exceptions

logging.basicConfig(level=logging.INFO)

API_TOKEN = "1812181211:AAExcppaKPw4EHpeNCzXtK9h3N9bkEvCm8w"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

menu_text = "Нейросеть Яндекса не знает, что говорит, и может сказать всякое — если что, не обижайтесь. " \
            "Распространяя получившиеся тексты, помните об ответственности. " \
            "Я никаким образом не отношусь к YaLM, все права принадлежат " \
            "Яндексу\n\n" \
            "Введите ваш текст:\n"


@dp.message_handler(commands=['start', 'help'], state='*')
async def send_welcome(message: types.Message):
    await States.NEUTRAL.set()
    await message.answer(
        "БалаБот\n\n"
        "Введи 'балабоба', чтобы начать\n"
    )


@dp.message_handler(lambda message: message.text.startswith('бала'), state=States.NEUTRAL)
async def bala(message: types.Message):
    await message.answer(menu_text, reply_markup=keyboard.back)
    await States.BALABOBA.set()


@dp.callback_query_handler(text="back", state='*')
async def _back(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await States.NEUTRAL.set()
    await call.message.answer(
        "БалаБот\n\n"
        "Введи 'балабоба', чтобы начать\n"
    )


@dp.message_handler(state=States.BALABOBA)
async def bala_wait(message: types.Message):
    await message.answer("Жди, работаю")
    await message.answer(balaboba.write(message.text))


@dp.message_handler(state='*')
async def dont_know(message: types.Message):
    await message.answer("Не знаю такую команду, давай заново")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
