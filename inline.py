from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
answ = dict()

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка', url='https://google.com')
x = [InlineKeyboardButton(text='ссылка 3', url='https://google.com'),
InlineKeyboardButton(text='ссылка 4', url='https://google.com'),
     InlineKeyboardButton(text='ссылка 5', url='https://google.com') ]
urlkb.add(urlButton,urlButton2).row(*x).insert(InlineKeyboardButton(text='ссылка2',url='https://google.com'))





@dp.message_handler(commands='ссылки')
async def url_commands(message: types.Message):
    await message.answer('Ссылочки', reply_markup=urlkb)


inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                             InlineKeyboardButton(text='He Like', callback_data='like_-1'))


@dp.message_handler(commands='test')
async def url_commands(message: types.Message):
    await message.answer('За видео про деплой бота', reply_markup=inkb)


@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)


    # await callback.message.answer('Нажата кнопка инлайн')
    # await callback.answer('Нажата кнопка инлайн', show_alert=True)


executor.start_polling(dp, skip_updates=True)
