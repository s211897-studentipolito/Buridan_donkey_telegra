import random, telebot

asino = telebot.TeleBot (TOKEN)

@asino.message_handler (commands=['start', 'help'])
def send_welcome (message):
    asino.reply_to(message, 'Insert two or more entry and I will choose for you!')

@asino.message_handler (func = lambda m: True)
def buridan (message):
    listB = message.text.split (' ')
    print (listB)
    rangeB = len(listB)
    reply = ''
    for i in range(rangeB):
        reply += str(i+1) + '. ' + listB.pop(random.randrange(0, len(listB))) + '\n'
    asino.send_message (message.chat.id, reply)

if __name__ == '__main__':
    while (1):
        try:
            asino.polling ()
        except:
            print ('crash ')
            pass
    asino.polling ()
