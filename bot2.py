import telegram
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
bot = telegram.Bot(token = '303806740:AAFM7baM6SiJaqwbx9-SW7YT9UvlBW6kqcM')
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
updater = Updater(token = '303806740:AAFM7baM6SiJaqwbx9-SW7YT9UvlBW6kqcM')
dispatcher = updater.dispatcher
import json

def start(bot, update):
	custom_keyboard = [['/menu', '/order', '/info']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Здравствуйте, %s, выберите одну из нижеприведенных команд:" % update.message.from_user.first_name, reply_markup = reply_markup)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def menu(bot, update):
	custom_keyboard = [['/Ciaopizza', '/Gingerpizza', '/Pizzahut'],
	['/Mangasushi', '/Samuraisushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Выберите пиццерию или суши-бар из нижеприведенных вариантов:", reply_markup = reply_markup)

from telegram.ext import CommandHandler
menu_handler = CommandHandler('menu', menu)
dispatcher.add_handler(menu_handler)


def Mangasushi(bot, update):
	custom_keyboard =[['/Rolls', '/Sushi', '/Order']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Выберите роллы или суши. После нажмите на кнопку 'Order' чтобы оформить заказ.", reply_markup = reply_markup)

def Rolls(bot, update):
	file = open("manga.json")
	menu = json.loads(file.read())
	for category in menu:
		products = menu[category]
		for p in products:
			bot.sendMessage(chat_id = update.message.chat_id, text = "Order_id:" + " " + str(p["data_id"]) + " " + p["name"] + " " + p["description"] + " " + "Цена:" + " " + str(p["price"]) + " " + "Количество роллов в одном сете:" + " " + str(p["quantity"]))
			keyboard = [[InlineKeyboardButton("Add to basket", callback_data='1'),
						InlineKeyboardButton("Delete from basket", callback_data='2')]]
			reply_markup = InlineKeyboardMarkup(keyboard)
			update.message.reply_text('Please choose:', reply_markup = reply_markup)

def Sushi(bot, update):
	file = open("manga.json")
	menu = json.loads(file.read())
	for category in menu:
		products = menu[category]
		for p in products:
			bot.sendMessage(chat_id = update.message.chat_id, text = "Order_id:" + " " + str(p["data_id"]) + " " + p["name"] + " " + p["description"] + " " + "Цена:" + " " + str(p["price"]) + " " + "Количество суши в одном сете:" + " " + str(p["quantity"]))
			keyboard = [[InlineKeyboardButton("Add to basket", callback_data='1'),
						InlineKeyboardButton("Delete from basket", callback_data='2')]]
			reply_markup = InlineKeyboardMarkup(keyboard)
			update.message.reply_text('Please choose:', reply_markup = reply_markup)
			#bot.sendPhoto(chat_id = chat_id, photo = p["img_url"])

from telegram.ext import CommandHandler
Rolls_handler = CommandHandler('Rolls', Rolls)
dispatcher.add_handler(Rolls_handler)

from telegram.ext import CommandHandler
Sushi_handler = CommandHandler('Sushi', Sushi)
dispatcher.add_handler(Sushi_handler)	

from telegram.ext import CommandHandler
Mangasushi_handler = CommandHandler('Mangasushi', Mangasushi)
dispatcher.add_handler(Mangasushi_handler)

def Order(bot, update):
	location_keyboard = telegram.KeyboardButton(text = "send_location", request_location = True)
	contact_keyboard = telegram.KeyboardButton(text = "send_contact", request_contact = True)
	email_keyboard = telegram.KeyboardButton(text = "send_email", request_email = True)
	custom_keyboard = [[location_keyboard, contact_keyboard, email_keyboard]]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Отправьте мне свой номер телефона и поделитесь местоположением", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Order_handler = CommandHandler('Order', Order)
dispatcher.add_handler(Order_handler)

def info(bot, update):
	wtext = "DAYorder - уникальный бот-проект, который поможет вам не только с выбором еды, а так же с оформлением заказа. Цель бота это сделать заказ, учитывая наиважнейшие критерии (цена, месторасположение, ингредиенты и тд.) не вовлекая лишних людей и глаз."
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

from telegram.ext import CommandHandler
info_handler = CommandHandler('info', info)
dispatcher.add_handler(info_handler)

#def log(message):
#	print("\n -----")
#	from datetime import datetime
#	print(datetime.now())
#	print("Сообщение от %s %s. (id = %d) \n Текст - (%s)" % update.message.from_user.first_name,
#															 update.message.from_user.last_name,
#															 update.message.from_user.id,
#															 update.message.text)
#@bot.message_handler(content_types=['text'])

def echo(bot, update):
	if "здравствуйте" in update.message.text.lower():
		wtext = "Здравствуйте, %s, выберите одну из нижеприведенных команд:" % update.message.from_user.first_name
		custom_keyboard = [['/menu', '/order', '/info']]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext, reply_markup = reply_markup)

	elif "здравствуй" in update.message.text.lower():
		wtext = "Здравствуй, %s, выбери одну из нижеприведенных команд:" % update.message.from_user.first_name
		custom_keyboard = [['/menu', '/order', '/info']]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext, reply_markup = reply_markup)

	elif "привет" in update.message.text.lower():
		wtext = "Приветствую, %s, выбери одну из нижеприведенных команд:" % update.message.from_user.first_name
		custom_keyboard = [['/menu', '/order', '/info']]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext, reply_markup = reply_markup)

	elif "салам" in update.message.text.lower():
		wtext = "По полам, %s-Родной, выбери одну из нижеприведенных команд:" % update.message.from_user.first_name
		custom_keyboard = [['/menu', '/order', '/info']]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext, reply_markup = reply_markup)


	elif "hello" in update.message.text.lower():
		wtext = "London is the capital of Great Britain" 
		custom_keyboard = [['/menu', '/order', '/info']]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext, reply_markup = reply_markup)

	elif "hi" in update.message.text.lower():
		wtext = "London is the capital of Great Britain" 
		custom_keyboard = [['/menu', '/order', '/info']]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext, reply_markup = reply_markup)

	elif "hey" in update.message.text.lower():
		wtext = "London is the capital of Great Britain" 
		custom_keyboard = [['/menu', '/order', '/info']]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext, reply_markup = reply_markup)

	elif "email" in update.message.text.lower():
		wtext = "Введите ваш email:"
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext)		

	else:
		wtext = "Салам Алейкум, %s, брат или сестренка, выбери одну из нижеприведенных команд:" % update.message.from_user.first_name
		custom_keyboard = [['/menu', '/order', '/info']]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext, reply_markup = reply_markup)
		log(message)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def contact(bot, update):
	print(update.message.contact)

from telegram.ext import MessageHandler, Filters
contact_handler = MessageHandler(Filters.contact, contact)
dispatcher.add_handler(contact_handler)

updater.start_polling()

