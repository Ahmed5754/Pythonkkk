import telebot
bot=telebot.TeleBot('7108892737:AAE3vcBs6jNiwWD_re0CN3AlF6MdgjVvXm8')
@bot.message_handler(commands=['start'])
def user(message):
    bot.send_message(message.chat.id, text="id : "+str(message.chat.id)+" \nuser :@"+str(message.from_user.username))
bot.polling()
