import telegram.ext


TOKEN = '5851369622:AAH9iuUTJs1aB20uJdNRLWRFWOfSQIesOfc'



def start(update, context):
    update.message.reply_text('''A bot repeating what you say''')

def content(update, context):
    update.message.reply_text('leave')

def handle_message(update, context):
    update.message.reply_text(f"you said {update.message.text}")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('content', content))

disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()