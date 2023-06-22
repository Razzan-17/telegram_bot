from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from init import TOKEN
from text import HELP_TEXT, START_TEXT
from method_db import MethodOnDateBase as mdb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

home_km = ReplyKeyboardMarkup(resize_keyboard=True,
                          row_width=3)
kb1 = KeyboardButton(text='/расход')
kb2 = KeyboardButton(text='/прибыль')
home_km.add(kb1, kb2)


def on_start():
    print('Я запустился!')


def on_shutdown():
    print('Пока')


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await mdb.register(message.from_user.id, message.from_user.first_name)
    print(message.from_user.first_name)
    await message.answer(text=START_TEXT + HELP_TEXT,
                         parse_mode='HTML',
                         reply_markup=home_km)


@dp.message_handler(commands=['help'])
async def start_cmd(message: types.Message):
    await message.answer(text=HELP_TEXT, parse_mode='HTML')


@dp.message_handler(commands=['трата'])
async def start_cmd(message: types.Message):
    data_l = message.text.split(' ')
    comment = None
    category = None
    if data_l[0].isdigit():
        summ = data_l[0]
        comment = ' '.join(data_l[1:])
        await message.answer(text=f'Запись {category}: {summ} сохранена')
    else:
        await message.answer(text='Напишите запрос вида: сумма - пробел - коментарий(если нужно)')


@dp.message_handler(commands=['прибыль'])
async def start_cmd(message: types.Message):
    print(message.text)
    await message.answer(text=message.text)


@dp.message_handler(commands=['all'])
async def start_cmd(message: types.Message):
    for operation in mdb.query_expense(message.from_user.id):
        response_text = f'{operation.spending_type} сумма: {operation.summ}'
        await message.answer(text=response_text)


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_start(),
                           on_shutdown=on_shutdown())
