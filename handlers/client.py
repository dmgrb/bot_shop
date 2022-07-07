from aiogram import types, Dispatcher
from data_base import sqlite_db
from create_bot import bot
from keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def comannd_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через л\с, \nhttps://t.me/Trany_bot')


# @dp.message_handler(commands=['Режим_работы'])
async def comannd_open(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Сб с 9.00 до 12.00')


# @dp.message_handler(commands=['Расположение'])
async def comannd_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Гавенная дом 18')


# @dp.register_message_handler(commands=['Меню'])
async def menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(comannd_start, commands=['start', 'help'])
    dp.register_message_handler(comannd_open, commands=['Режим_работы'])
    dp.register_message_handler(comannd_place, commands=['Расположение'])
    dp.register_message_handler(menu_command, commands=['Меню'])
