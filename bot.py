import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
	bot.sent_message(message.chat.id, message.text)

# RUN
bot.polling(non_stop=True)