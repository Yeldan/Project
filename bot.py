import telegram
import telebot
import constants
bot = telegram.Bot(token = '303806740:AAFM7baM6SiJaqwbx9-SW7YT9UvlBW6kqcM')
from telegram.ext import Updater
updater = Updater(token = '303806740:AAFM7baM6SiJaqwbx9-SW7YT9UvlBW6kqcM')
dispatcher = updater.dispatcher

#status = {}
#status[user_id] = {
#	'rest_id': 
#	'a'
#}

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

def Ciaopizza(bot, update):
	custom_keyboard = [['/Mamamia', '/Pepperoni', '/Margarita'],
	['/ChetireSezona', '/Chaopizza', '/menu']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Выберите пиццу из нижеприведенных вариантов, либо нажмите на кнопку 'menu', если хотите вернуться к выбору пиццерии или суши-бара.", reply_markup = reply_markup)
	
def Mamamia(bot, update):
	custom_keyboard = [['/Price1_1', '/Description1_1', '/order'], 
	['/Ciaopizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Ciaopizza', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price1_1(bot, update):
	custom_keyboard = [['/order', '/Mamamia']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "2710 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price1_1_handler = CommandHandler('Price1_1', Price1_1)
dispatcher.add_handler(Price1_1_handler)

def Description1_1(bot, update):
	custom_keyboard = [['/order', '/Mamamia']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Семга, пицца-соус, сыр.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description1_1_handler = CommandHandler('Description1_1', Description1_1)
dispatcher.add_handler(Description1_1_handler)

def Pepperoni(bot, update):
	custom_keyboard = [['/Price1_2', '/Description1_2', '/order'], 
	['/Ciaopizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Ciaopizza', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price1_2(bot, update):
	custom_keyboard = [['/order', '/Pepperoni']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "2200 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price1_2_handler = CommandHandler('Price1_2', Price1_2)
dispatcher.add_handler(Price1_2_handler)

def Description1_2(bot, update):
	custom_keyboard = [['/order', '/Pepperoni']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Салями, пицца-соус, сыр.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description1_2_handler = CommandHandler('Description1_2', Description1_2)
dispatcher.add_handler(Description1_2_handler)

def Margarita(bot, update):
	custom_keyboard = [['/Price1_3', '/Description1_3', '/order'], 
	['/Ciaopizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Ciaopizza', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price1_3(bot, update):
	custom_keyboard = [['/order', '/Margarita']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "1850 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price1_3_handler = CommandHandler('Price1_3', Price1_3)
dispatcher.add_handler(Price1_3_handler)

def Description1_3(bot, update):
	custom_keyboard = [['/order', '/Margarita']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Пицца-соус, сыр.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description1_3_handler = CommandHandler('Description1_3', Description1_3)
dispatcher.add_handler(Description1_3_handler)

def ChetireSezona(bot, update):
	custom_keyboard = [['/Price1_4', '/Description1_4', '/order'], 
	['/Ciaopizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Ciaopizza', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price1_4(bot, update):
	custom_keyboard = [['/order', '/ChetireSezona']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "2540 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price1_4_handler = CommandHandler('Price1_4', Price1_4)
dispatcher.add_handler(Price1_4_handler)

def Description1_4(bot, update):
	custom_keyboard = [['/order', '/ChetireSezona']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Ветчина, грибы, маслины, овощи, пицца-соус, сыр.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description1_4_handler = CommandHandler('Description1_4', Description1_4)
dispatcher.add_handler(Description1_4_handler)

def Chaopizza(bot, update):
	custom_keyboard = [['/Price1_5', '/Description1_5', '/order'], 
	['/Ciaopizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Ciaopizza', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price1_5(bot, update):
	custom_keyboard = [['/order', '/Chaopizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "2190 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price1_5_handler = CommandHandler('Price1_5', Price1_5)
dispatcher.add_handler(Price1_5_handler)

def Description1_5(bot, update):
	custom_keyboard = [['/order', '/Chaopizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Ветчина, грибы, кукуруза, перец болгарский, сливочный соус, сыр.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description1_5_handler = CommandHandler('Description1_5', Description1_5)
dispatcher.add_handler(Description1_5_handler)

from telegram.ext import CommandHandler
Mamamia_handler = CommandHandler('Mamamia', Mamamia)
dispatcher.add_handler(Mamamia_handler)

from telegram.ext import CommandHandler
Pepperoni_handler = CommandHandler('Pepperoni', Pepperoni)
dispatcher.add_handler(Pepperoni_handler)

from telegram.ext import CommandHandler
Margarita_handler = CommandHandler('Margarita', Margarita)
dispatcher.add_handler(Margarita_handler)

from telegram.ext import CommandHandler
ChetireSezona_handler = CommandHandler('ChetireSezona', ChetireSezona)
dispatcher.add_handler(ChetireSezona_handler)

from telegram.ext import CommandHandler
Chaopizza_handler = CommandHandler('Chaopizza', Chaopizza)
dispatcher.add_handler(Chaopizza_handler)

from telegram.ext import CommandHandler
Ciaopizza_handler = CommandHandler('Ciaopizza', Ciaopizza)
dispatcher.add_handler(Ciaopizza_handler)

def Gingerpizza(bot, update):
	custom_keyboard = [['/Bolognese', '/Margarita2', '/Ginger'],
	['/ShestSirov', '/BBQ', '/menu']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Выберите пиццу из нижеприведенных вариантов, либо нажмите на кнопку 'menu', если хотите вернуться к выбору пиццерии или суши-бара.", reply_markup = reply_markup)

def Bolognese(bot, update):
	custom_keyboard = [['/Price2_1', '/Description2_1', '/order'], 
	['/Gingerpizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Gingerpizza', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price2_1(bot, update):
	custom_keyboard = [['/order', '/Bolognese']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "1899 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price2_1_handler = CommandHandler('Price2_1', Price2_1)
dispatcher.add_handler(Price2_1_handler)

def Description2_1(bot, update):
	custom_keyboard = [['/order', '/Bolognese']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Фарш говяжий, соус, сыр моцарелла, жгучий перец (на выбор).", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description2_1_handler = CommandHandler('Description2_1', Description2_1)
dispatcher.add_handler(Description2_1_handler)

def Margarita2(bot, update):
	custom_keyboard = [['/Price2_2', '/Description2_2', '/order'], 
	['/Gingerpizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Gingerpizza', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price2_2(bot, update):
	custom_keyboard = [['/order', '/Margarita2']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "1379 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price2_2_handler = CommandHandler('Price2_2', Price2_2)
dispatcher.add_handler(Price2_2_handler)

def Description2_2(bot, update):
	custom_keyboard = [['/order', '/Margarita2']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Помидор, сыр Моцарелла, пицца-соус, базилик, орегано.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description2_2_handler = CommandHandler('Description2_2', Description2_2)
dispatcher.add_handler(Description2_2_handler)

def Ginger(bot, update):
	custom_keyboard = [['/Price2_3', '/Description2_3', '/order'], 
	['/Gingerpizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Gingerpizza', если хотите выбрать другую пиццу.", reply_markup = reply_markup)	

def Price2_3(bot, update):
	custom_keyboard = [['/order', '/Ginger']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "2099 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price2_3_handler = CommandHandler('Price2_3', Price2_3)
dispatcher.add_handler(Price2_3_handler)

def Description2_3(bot, update):
	custom_keyboard = [['/order', '/Ginger']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Фарш, филе куриное, салями, перец болгарский, перец халапенью, сыр моцарелла.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description2_3_handler = CommandHandler('Description2_3', Description2_3)
dispatcher.add_handler(Description2_3_handler)

def ShestSirov(bot, update):
	custom_keyboard = [['/Price2_4', '/Description2_4', '/order'], 
	['/Gingerpizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Gingerpizza', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price2_4(bot, update):
	custom_keyboard = [['/order', '/ShestSirov']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "2099 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price2_4_handler = CommandHandler('Price2_4', Price2_4)
dispatcher.add_handler(Price2_4_handler)

def Description2_4(bot, update):
	custom_keyboard = [['/order', '/ShestSirov']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Сыр Моцарелла, сыр Эдам, Сыр Гауда, сыр Дор блю(с плесенью), сыр Тильзиттер, сыр Пармезан, пицца-соус.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description2_4_handler = CommandHandler('Description2_4', Description2_4)
dispatcher.add_handler(Description2_4_handler)

def BBQ(bot, update):
	custom_keyboard = [['/Price2_5', '/Description2_5', '/order'], 
	['/Ciaopizza']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Gingerpizza', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price2_5(bot, update):
	custom_keyboard = [['/order', '/BBQ']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "1699 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price2_5_handler = CommandHandler('Price2_5', Price2_5)
dispatcher.add_handler(Price2_5_handler)

def Description2_5(bot, update):
	custom_keyboard = [['/order', '/BBQ']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Кабаноси, куриное филе, сыр Моцарелла, сыр Гауда, Сыр Тильзиттер, брокколи, соус BBQ со жгучим перцем Чили (на ваш выбор), пицца-соус.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description2_5_handler = CommandHandler('Description2_5', Description2_5)
dispatcher.add_handler(Description2_5_handler)

from telegram.ext import CommandHandler
Bolognese_handler = CommandHandler('Bolognese', Bolognese)
dispatcher.add_handler(Bolognese_handler)

from telegram.ext import CommandHandler
Margarita2_handler = CommandHandler('Margarita2', Margarita2)
dispatcher.add_handler(Margarita2_handler)

from telegram.ext import CommandHandler
Ginger_handler = CommandHandler('Ginger', Ginger)
dispatcher.add_handler(Ginger_handler)

from telegram.ext import CommandHandler
ShestSirov_handler = CommandHandler('ShestSirov', ShestSirov)
dispatcher.add_handler(ShestSirov_handler)

from telegram.ext import CommandHandler
BBQ_handler = CommandHandler('BBQ', BBQ)
dispatcher.add_handler(BBQ_handler)

from telegram.ext import CommandHandler
Gingerpizza_handler = CommandHandler('Gingerpizza', Gingerpizza)
dispatcher.add_handler(Gingerpizza_handler)

def Pizzahut(bot, update):
	custom_keyboard = [['/SpicyCurry', '/Pepperoni2', '/Kurinaya'],
	['/Margarita3', '/BBQ2', '/menu']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Выберите пиццу из нижеприведенных вариантов, либо нажмите на кнопку 'menu', если хотите вернуться к выбору пиццерии или суши-бара.", reply_markup = reply_markup)

def SpicyCurry(bot, update):
	custom_keyboard = [['/Price3_1', '/Description3_1', '/order'], 
	['/Pizzahut']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Pizzahut', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price3_1(bot, update):
	custom_keyboard = [['/order', '/SpicyCurry']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "2300 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price3_1_handler = CommandHandler('Price3_1', Price3_1)
dispatcher.add_handler(Price3_1_handler)

def Description3_1(bot, update):
	custom_keyboard = [['/order', '/SpicyCurry']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Яркая смесь овощей, куриного филе и соуса из пряных специй слились воедино на тонком хрустящем тесте в жаркой композиции «Spicy Curry».", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description3_1_handler = CommandHandler('Description3_1', Description3_1)
dispatcher.add_handler(Description3_1_handler)

def Pepperoni2(bot, update):
	custom_keyboard = [['/Price3_2', '/Description3_2', '/order'], 
	['/Pizzahut']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Pizzahut', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price3_2(bot, update):
	custom_keyboard = [['/order', '/Pepperoni2']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "2200 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price3_2_handler = CommandHandler('Price3_2', Price3_2)
dispatcher.add_handler(Price3_2_handler)

def Description3_2(bot, update):
	custom_keyboard = [['/order', '/Pepperoni2']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Разделите с друзьями пиццу с колбасой пепперони, томатным соусом и сыром Моцарелла.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description3_2_handler = CommandHandler('Description3_2', Description3_2)
dispatcher.add_handler(Description3_2_handler)

def Kurinaya(bot,update):
	custom_keyboard = [['/Price3_3', '/Description3_3', '/order'], 
	['/Pizzahut']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Pizzahut', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price3_3(bot, update):
	custom_keyboard = [['/order', '/Kurinaya']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "2300 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price3_3_handler = CommandHandler('Price3_3', Price3_3)
dispatcher.add_handler(Price3_3_handler)

def Description3_3(bot, update):
	custom_keyboard = [['/order', '/Kurinaya']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Отметьте аромат нежнейшего филе жареного цыпленка с томатным соусом, болгарским перцем, луком, свежими помидорами и сыром Моцарелла.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description3_3_handler = CommandHandler('Description3_3', Description3_3)
dispatcher.add_handler(Description3_3_handler)

def Margarita3(bot, update):
	custom_keyboard = [['/Price3_4', '/Description3_4', '/order'], 
	['/Pizzahut']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Pizzahut', если хотите выбрать другую пиццу.", reply_markup = reply_markup)	

def Price3_4(bot, update):
	custom_keyboard = [['/order', '/Margarita3']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "1700 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price3_4_handler = CommandHandler('Price3_4', Price3_4)
dispatcher.add_handler(Price3_4_handler)

def Description3_4(bot, update):
	custom_keyboard = [['/order', '/Margarita3']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Маргарита с томатным соусом и сыром Моцарелла.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description3_4_handler = CommandHandler('Description3_4', Description3_4)
dispatcher.add_handler(Description3_4_handler)

def BBQ2(bot, update):
	custom_keyboard = [['/Price3_5', '/Description3_5', '/order'], 
	['/Pizzahut']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Pizzahut', если хотите выбрать другую пиццу.", reply_markup = reply_markup)

def Price3_5(bot, update):
	custom_keyboard = [['/order', '/BBQ2']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "2300 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price3_5_handler = CommandHandler('Price3_5', Price3_5)
dispatcher.add_handler(Price3_5_handler)

def Description3_5(bot, update):
	custom_keyboard = [['/order', '/BBQ2']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Почувствуйте аромат пикника. Великолепное сочетание сыра Моцарелла с Пепперони (колбаса), говядиной, луком и соусом Барбекю.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description3_5_handler = CommandHandler('Description3_5', Description3_5)
dispatcher.add_handler(Description3_5_handler)

from telegram.ext import CommandHandler
SpicyCurry_handler = CommandHandler('SpicyCurry', SpicyCurry)
dispatcher.add_handler(SpicyCurry_handler)

from telegram.ext import CommandHandler
Pepperoni2_handler = CommandHandler('Pepperoni2', Pepperoni2)
dispatcher.add_handler(Pepperoni2_handler)

from telegram.ext import CommandHandler
Kurinaya_handler = CommandHandler('Kurinaya', Kurinaya)
dispatcher.add_handler(Kurinaya_handler)

from telegram.ext import CommandHandler
Margarita3_handler = CommandHandler('Margarita3', Margarita3)
dispatcher.add_handler(Margarita3_handler)

from telegram.ext import CommandHandler
BBQ2_handler = CommandHandler('BBQ2', BBQ2)
dispatcher.add_handler(BBQ2_handler)

from telegram.ext import CommandHandler
Pizzahut_handler = CommandHandler('Pizzahut', Pizzahut)
dispatcher.add_handler(Pizzahut_handler)

def Mangasushi(bot, update):
	custom_keyboard = [['/Fila', '/CALIFORNIMATION', '/LososTempura'],
	['/UgorTempura', '/RollsOgurcom', '/menu']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Выберите суши из нижеприведенных вариантов, либо нажмите на кнопку 'menu', если хотите вернуться к выбору пиццерии или суши-бара.", reply_markup = reply_markup)

def Fila(bot, update):
	custom_keyboard = [['/Price4_1', '/Description4_1', '/order'], 
	['/Mangasushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Mangasushi', если хотите выбрать другии суши.", reply_markup = reply_markup)

def Price4_1(bot, update):
	custom_keyboard = [['/order', '/Fila']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "1500 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price4_1_handler = CommandHandler('Price4_1', Price4_1)
dispatcher.add_handler(Price4_1_handler)

def Description4_1(bot, update):
	custom_keyboard = [['/order', '/Fila']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Классический ролл с лососем и сливочным сыром.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description4_1_handler = CommandHandler('Description4_1', Description4_1)
dispatcher.add_handler(Description4_1_handler)

def CALIFORNIMATION(bot, update):
	custom_keyboard = [['/Price4_2', '/Description4_2', '/order'], 
	['/Mangasushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Mangasushi', если хотите выбрать другии суши.", reply_markup = reply_markup)

def Price4_2(bot, update):
	custom_keyboard = [['/order', '/CALIFORNIMATION']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "1150 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price4_2_handler = CommandHandler('Price4_2', Price4_2)
dispatcher.add_handler(Price4_2_handler)

def Description4_2(bot, update):
	custom_keyboard = [['/order', '/CALIFORNIMATION']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Классический ролл с крабовым миксом, авокадо и огурцом.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description4_2_handler = CommandHandler('Description4_2', Description4_2)
dispatcher.add_handler(Description4_2_handler)

def LososTempura(bot, update):
	custom_keyboard = [['/Price4_3', '/Description4_3', '/order'], 
	['/Mangasushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Mangasushi', если хотите выбрать другии суши.", reply_markup = reply_markup)

def Price4_3(bot, update):
	custom_keyboard = [['/order', '/LososTempura']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "900 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price4_3_handler = CommandHandler('Price4_3', Price4_3)
dispatcher.add_handler(Price4_3_handler)

def Description4_3(bot, update):
	custom_keyboard = [['/order', '/LososTempura']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Хрустящий ролл с лососем и сливочным сыром.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description4_3_handler = CommandHandler('Description4_3', Description4_3)
dispatcher.add_handler(Description4_3_handler)

def UgorTempura(bot, update):
	custom_keyboard = [['/Price4_4', '/Description4_4', '/order'], 
	['/Mangasushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Mangasushi', если хотите выбрать другии суши.", reply_markup = reply_markup)

def Price4_4(bot, update):
	custom_keyboard = [['/order', '/UgorTempura']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "1350 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price4_4_handler = CommandHandler('Price4_4', Price4_4)
dispatcher.add_handler(Price4_4_handler)

def Description4_4(bot, update):
	custom_keyboard = [['/order', '/UgorTempura']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Теплый ролл с угрем и сливочным сыром.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description4_4_handler = CommandHandler('Description4_4', Description4_4)
dispatcher.add_handler(Description4_4_handler)

def RollsOgurcom(bot, update):
	custom_keyboard = [['/Price4_5', '/Description4_5', '/order'], 
	['/Mangasushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Mangasushi', если хотите выбрать другии суши.", reply_markup = reply_markup)

def Price4_5(bot, update):
	custom_keyboard = [['/order', '/RollsOgurcom']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "250 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price4_5_handler = CommandHandler('Price4_5', Price4_5)
dispatcher.add_handler(Price4_5_handler)

def Description4_5(bot, update):
	custom_keyboard = [['/order', '/RollsOgurcom']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Маленький ролл с огурцом, рисом и нори.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description4_5_handler = CommandHandler('Description4_5', Description4_5)
dispatcher.add_handler(Description4_5_handler)

from telegram.ext import CommandHandler
Fila_handler = CommandHandler('Fila', Fila)
dispatcher.add_handler(Fila_handler)

from telegram.ext import CommandHandler
CALIFORNIMATION_handler = CommandHandler('CALIFORNIMATION', CALIFORNIMATION)
dispatcher.add_handler(CALIFORNIMATION_handler)

from telegram.ext import CommandHandler
LososTempura_handler = CommandHandler('LososTempura', LososTempura)
dispatcher.add_handler(LososTempura_handler)

from telegram.ext import CommandHandler
UgorTempura_handler = CommandHandler('UgorTempura', UgorTempura)
dispatcher.add_handler(UgorTempura_handler)

from telegram.ext import CommandHandler
RollsOgurcom_handler = CommandHandler('RollsOgurcom', RollsOgurcom)
dispatcher.add_handler(RollsOgurcom_handler)

from telegram.ext import CommandHandler
Mangasushi_handler = CommandHandler('Mangasushi', Mangasushi)
dispatcher.add_handler(Mangasushi_handler)

def Samuraisushi(bot, update):
	custom_keyboard = [['/FiladelfiyaMaki', '/EbiTempuraMaki', '/OsakaTempuraMaki'],
	['/SutoMakisLososemiOmletom', '/KappaMakisOgurcom', '/menu']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Выберите суши из нижеприведенных вариантов, либо нажмите на кнопку 'menu', если хотите вернуться к выбору пиццерии или суши-бара.", reply_markup = reply_markup)

def FiladelfiyaMaki(bot, update):
	custom_keyboard = [['/Price5_1', '/Description5_1', '/order'], 
	['/Samuraisushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Samuraisushi', если хотите выбрать другии суши.", reply_markup = reply_markup)

def Price5_1(bot, update):
	custom_keyboard = [['/order', '/FiladelfiyaMaki']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "1099 тг ", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price5_1_handler = CommandHandler('Price5_1', Price5_1)
dispatcher.add_handler(Price5_1_handler)

def Description5_1(bot, update):
	custom_keyboard = [['/order', '/FiladelfiyaMaki']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Ролл с сыром филадельфия и филе лосося.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description5_1_handler = CommandHandler('Description5_1', Description5_1)
dispatcher.add_handler(Description5_1_handler)

def EbiTempuraMaki(bot, update):
	custom_keyboard = [['/Price5_2', '/Description5_2', '/order'], 
	['/Samuraisushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Samuraisushi', если хотите выбрать другии суши.", reply_markup = reply_markup)

def Price5_2(bot, update):
	custom_keyboard = [['/order', '/EbiTempuraMaki']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "799 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price5_2_handler = CommandHandler('Price5_2', Price5_2)
dispatcher.add_handler(Price5_2_handler)

def Description5_2(bot, update):
	custom_keyboard = [['/order', '/EbiTempuraMaki']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Теплый ролл с королевскими креветками и сливочным сыром.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description5_2_handler = CommandHandler('Description5_2', Description5_2)
dispatcher.add_handler(Description5_2_handler)

def OsakaTempuraMaki(bot, update):
	custom_keyboard = [['/Price5_3', '/Description5_3', '/order'], 
	['/Samuraisushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Samuraisushi', если хотите выбрать другии суши.", reply_markup = reply_markup)

def Price5_3(bot, update):
	custom_keyboard = [['/order', '/OsakaTempuraMaki']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "899 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price5_3_handler = CommandHandler('Price5_3', Price5_3)
dispatcher.add_handler(Price5_3_handler)

def Description5_3(bot, update):
	custom_keyboard = [['/order', '/OsakaTempuraMaki']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Теплый ролл с копченым угрем и сливочным сыром филадельфия.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description5_3_handler = CommandHandler('Description5_3', Description5_3)
dispatcher.add_handler(Description5_3_handler)

def SutoMakisLososemiOmletom(bot, update):
	custom_keyboard = [['/Price5_4', '/Description5_4', '/order'], 
	['/Samuraisushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Samuraisushi', если хотите выбрать другии суши.", reply_markup = reply_markup)

def Price5_4(bot, update):
	custom_keyboard = [['/order', '/SutoMakisLososemiOmletom']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "399 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price5_4_handler = CommandHandler('Price5_4', Price5_4)
dispatcher.add_handler(Price5_4_handler)

def Description5_4(bot, update):
	custom_keyboard = [['/order', '/SutoMakisLososemiOmletom']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Маленькие роллы с лососем и омлетом.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description5_4_handler = CommandHandler('Description5_4', Description5_4)
dispatcher.add_handler(Description5_4_handler)

def KappaMakisOgurcom(bot, update):
	custom_keyboard = [['/Price5_5', '/Description5_5', '/order'], 
	['/Samuraisushi']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Посмотрите цену, описание, либо сразу оформите заказ, либо нажмите на кнопку 'Samuraisushi', если хотите выбрать другии суши.", reply_markup = reply_markup)

def Price5_5(bot, update):
	custom_keyboard = [['/order', '/KappaMakisOgurcom']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "199 тг", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Price5_5_handler = CommandHandler('Price5_5', Price5_5)
dispatcher.add_handler(Price5_5_handler)

def Description5_5(bot, update):
	custom_keyboard = [['/order', '/KappaMakisOgurcom']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Маленькие роллы с огурцом.", reply_markup = reply_markup)

from telegram.ext import CommandHandler
Description5_5_handler = CommandHandler('Description5_5', Description5_5)
dispatcher.add_handler(Description5_5_handler)

from telegram.ext import CommandHandler
FiladelfiyaMaki_handler = CommandHandler('FiladelfiyaMaki', FiladelfiyaMaki)
dispatcher.add_handler(FiladelfiyaMaki_handler)

from telegram.ext import CommandHandler
EbiTempuraMaki_handler = CommandHandler('EbiTempuraMaki', EbiTempuraMaki)
dispatcher.add_handler(EbiTempuraMaki_handler)

from telegram.ext import CommandHandler
OsakaTempuraMaki_handler = CommandHandler('OsakaTempuraMaki', OsakaTempuraMaki)
dispatcher.add_handler(OsakaTempuraMaki_handler)

from telegram.ext import CommandHandler
SutoMakisLososemiOmletom_handler = CommandHandler('SutoMakisLososemiOmletom', SutoMakisLososemiOmletom)
dispatcher.add_handler(SutoMakisLososemiOmletom_handler)

from telegram.ext import CommandHandler
KappaMakisOgurcom_handler = CommandHandler('KappaMakisOgurcom', KappaMakisOgurcom)
dispatcher.add_handler(KappaMakisOgurcom_handler)

from telegram.ext import CommandHandler
Samuraisushi_handler = CommandHandler('Samuraisushi', Samuraisushi)
dispatcher.add_handler(Samuraisushi_handler)

from telegram.ext import CommandHandler
menu_handler = CommandHandler('menu', menu)
dispatcher.add_handler(menu_handler)

#def order4(bot, update):

#def order3(bot, update):

def order(bot, update):
	wtext = "Пожалуйста заполните свои данные через запятую: ФИО:, Адрес:, Номер телефона:, email:, Комментарии(Необязательно): . Пример: Назарбаев Нурсултан, Белый дом 2, +7 (777) 777 77 77, naziktop@gmail.com, Побольше соли пожалуйста. "                                                                                                                                     
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

#def order2(bot, update):
	#wtext = "name, adress, phone, email, comments"
	#bot.sendMessage(chat_id = update.message.chat_id, text = wtext)	

#def order1(bot, update):


from telegram.ext import CommandHandler
order_handler = CommandHandler('order', order)
dispatcher.add_handler(order_handler)

def info(bot, update):
	wtext = "DAYorder - уникальный бот-проект, который поможет вам не только с выбором еды, а так же с оформлением заказа. Цель бота это сделать заказ, учитывая наиважнейшие критерии (цена, месторасположение, ингредиенты и тд.) не вовлекая лишних людей и глаз."
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

from telegram.ext import CommandHandler
info_handler = CommandHandler('info', info)
dispatcher.add_handler(info_handler)

def log(message):
	print("\n -----")
	from datetime import datetime
	print(datetime.now())
	print("Сообщение от %s %s. (id = %d) \n Текст - (%s)" % update.message.from_user.first_name,
		                                                     update.message.from_user.last_name,
		                                                     update.message.from_user.id,
		                                                     update.message.text)
@bot.message_handler(content_types=['text'])
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

	else:
		wtext = "Салам Алейкум, %s, брат или сестренка, выбери одну из нижеприведенных команд:" % update.message.from_user.first_name
		custom_keyboard = [['/menu', '/order', '/info']]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext, reply_markup = reply_markup)
		log(message)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()

