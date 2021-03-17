
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot





    ############################
API_TOKEN = '1702185841:AAHTh9yhMMG-EhlLIE_2_bkbLY0KgqgLq8M'

bot = telebot.TeleBot(API_TOKEN)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    print(message)
    text_answer_message = """\
    Hi there, I am EchoBot.
    I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
    """
    bot.reply_to(message, text_answer_message)




# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    bot.send_message(message.chat.id, message.chat.id)


bot.polling()