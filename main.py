
import telebot
from telebot import types
from telebot import apihelper
import config
from f1calendar import upcomingraces, deferredraces, canceledraces
from stock_information import courses
from stock_charts import forex_chart
#from stock_information import stock_information

bot = telebot.TeleBot(config.token) #создали бота

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('images\sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Привет!\nМеня создал парень, который работает в банке и увлекается королевскими автогонками!\nЯ умею присылать биржевую информацию и календарь гонок Формулы 1.\nТы можешь увидеть все мои команды нажав на </>, а также нажав на /help.\nПоехали!!!")

@bot.message_handler(commands=['f1_calendar'])
def f1_calendar(message):

  key = types.InlineKeyboardMarkup()
  but_1 = types.InlineKeyboardButton(text="Предстоящие гран-при", callback_data="Предстоящие гран-при")
  but_2 = types.InlineKeyboardButton(text="Отложенные гран-при", callback_data="Отложенные гран-при")
  but_3 = types.InlineKeyboardButton(text="Отмененные гран-при", callback_data="Отмененные гран-при")
  key.add(but_1)
  key.add(but_2)
  key.add(but_3)
  bot.send_message(message.chat.id, "Список каких гран-при ты хочешь увидеть?", reply_markup=key)
    
@bot.message_handler(commands=['stock_information'])
def stock_information(message):
      
  key = types.InlineKeyboardMarkup()
  but_1 = types.InlineKeyboardButton(text="Австралийский доллар", callback_data="AUD")
  but_2 = types.InlineKeyboardButton(text="Белорусский рубль", callback_data="BYN")
  but_3 = types.InlineKeyboardButton(text="Доллар США", callback_data="USD")
  but_4 = types.InlineKeyboardButton(text="Евро", callback_data="EUR")
  but_5 = types.InlineKeyboardButton(text="Канадский доллар", callback_data="CAD")
  but_6 = types.InlineKeyboardButton(text="Китайский юань", callback_data="CNY")
  but_7 = types.InlineKeyboardButton(text="Сингапурский доллар", callback_data="SGD")
  but_8 = types.InlineKeyboardButton(text="Фунт стерлингов", callback_data="GBP")
  key.add(but_1)
  key.add(but_2)
  key.add(but_3)
  key.add(but_4)
  key.add(but_5)
  key.add(but_6)
  key.add(but_7)
  key.add(but_8)
  bot.send_message(message.chat.id, "Курс какой валюты ты хочешь узнать?", reply_markup=key)

@bot.message_handler(commands=['stock_charts'])
def stock_information(message):
      
  key = types.InlineKeyboardMarkup()
  but_1 = types.InlineKeyboardButton(text="Курс Доллара США за месяц", callback_data="USDRUBmonth")
  but_2 = types.InlineKeyboardButton(text="Курс Евро за месяц", callback_data="EURRUBmonth")
  but_3 = types.InlineKeyboardButton(text="Курс Доллара США за год", callback_data="USDRUByear")
  but_4 = types.InlineKeyboardButton(text="Курс Евро за год", callback_data="EURRUByear")
  key.add(but_1)
  key.add(but_2)
  key.add(but_3)
  key.add(but_4)
  bot.send_message(message.chat.id, "Какой график ты хочешь увидеть?", reply_markup=key)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/f1_calendar - получение данных об этапах чемпионата мира Формулы 1\n/stock_information - получение данных о курсах валют\n/stock_charts - графики курса Евро и Доллара США\n/help - справочная информация по боту")

@bot.callback_query_handler(func=lambda call: True)
def callBack(call):
  if call.data == 'Предстоящие гран-при':
    bot.send_message(call.message.chat.id,"Предстоящие гран-при:\n\n{}".format(upcomingraces()))
  elif call.data == 'Отложенные гран-при':
    bot.send_message(call.message.chat.id, "Отложенные гран-при:\n\n{}".format(deferredraces()))
  elif call.data == 'Отмененные гран-при':
    bot.send_message(call.message.chat.id, "Отмененные гран-при:\n\n{}".format(canceledraces()))
  elif call.data == 'AUD':
    bot.send_message(call.message.chat.id, "Текущий курс Австралийкого доллара (AUD) по данным ЦБ РФ:\n{} ₽".format(courses('Австралийский доллар')))
  elif call.data == 'BYN':
    bot.send_message(call.message.chat.id, "Текущий курс Белорусского рубля по данным ЦБ РФ:\n{} ₽".format(courses('Белорусский рубль')))
  elif call.data == 'USD':
    bot.send_message(call.message.chat.id, "Текущий курс Доллара США (USD) по данным ЦБ РФ:\n{} ₽".format(courses('Доллар США')))
  elif call.data == 'EUR':
    bot.send_message(call.message.chat.id, "Текущий курс Евро по данным ЦБ РФ:\n{} ₽".format(courses('Евро')))
  elif call.data == 'CAD':
    bot.send_message(call.message.chat.id, "Текущий курс Канадского доллара (CAD) по данным ЦБ РФ:\n{} ₽".format(courses('Канадский доллар')))
  elif call.data == 'CNY':
    bot.send_message(call.message.chat.id, "Текущий курс Китайской юани по данным ЦБ РФ:\n{} ₽".format(courses('Китайский юань')))
  elif call.data == 'SGD':
    bot.send_message(call.message.chat.id, "Текущий курс Сингапурского доллара (SGD) по данным ЦБ РФ:\n{} ₽".format(courses('Сингапурский доллар')))
  elif call.data == 'GBP':
    bot.send_message(call.message.chat.id, "Текущий курс Британского фунта по данным ЦБ РФ:\n{} ₽".format(courses('Фунт стерлингов')))
  elif call.data == 'USDRUBmonth':
    forex_chart(0, 0)
    img = open('plt.png', 'rb')
    bot.send_photo(call.message.chat.id, img)
  elif call.data == 'EURRUBmonth':
    forex_chart(1, 0)
    img = open('plt.png', 'rb')
    bot.send_photo(call.message.chat.id, img)
  elif call.data == 'USDRUByear':
    forex_chart(0, 1)
    img = open('plt.png', 'rb')
    bot.send_photo(call.message.chat.id, img)
  elif call.data == 'EURRUByear':
    forex_chart(1, 1)
    img = open('plt.png', 'rb')
    bot.send_photo(call.message.chat.id, img)


@bot.message_handler(func=lambda message: message.text not in ('/start', '/f1_calendar', 'stock_information', 'stock_charts', '/help'))
def cmd_sample_message(message):
    bot.send_message(message.chat.id, "К сожалению я могу отвечать только на конкретные команды(\n"
                                      "Список команды вы сможете найти кликнув по ссылке /help")

bot.polling(none_stop=True)
