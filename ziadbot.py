import telegram.ext
import requests



TOKEN = '5851369622:AAH9iuUTJs1aB20uJdNRLWRFWOfSQIesOfc'

def get_user_text(message):
    params = {
        'access_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiOTNlOWVkODIxNWU2MWY2ODdmMTEyZTI5YzE2ZjRiMTVkYWZkMWE5MmRhMWFjNWVmNGM3NGMyMzc1Mjc4NzM4MTY4NTM2ZWUxMDNlMmJlZjQiLCJpYXQiOjE2NzA1MDgwMTYsIm5iZiI6MTY3MDUwODAxNiwiZXhwIjoxNzAyMDQ0MDE2LCJzdWIiOiIxOTE2NCIsInNjb3BlcyI6W119.OVltlFiXqYVKpl-bdUfs1yXxdoyI_k7ovgzRWKi-UXp0CDW4GeMLjHyfKtd-HO8gcH2TYmPBtnKJCQmP9Y7dtg',
        'flightIata': message.text
    }
    
    api_result = requests.get('https://app.goflightlabs.com/advanced-real-time-flights', params)
    try:
        fetch = api_result.json()['data'][0]['status']
    except:
        fetch = "I can't find this flight"
instance = get_user_text(update.message)

def start(update, context):
    update.message.reply_text('''A bot repeating what you say''')

def content(update, context):
    update.message.reply_text('leave')

def handle_message(update, context):
    update.message.reply_text(instance)

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('content', content))

disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()
