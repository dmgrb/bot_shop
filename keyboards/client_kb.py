from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
#b4 = KeyboardButton('Поделится номером', request_contact=True)
#b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
#размер клавиатуры; клава пряется после ввода

kb_client.add(b1).add(b2).insert(b3)\
    #.row(b4,b5)

#kb_client.row(b1,b2,b3) #в одну строку
#kb_client.add(b1).add(b2).insert(b3) # отдельными кнопками
