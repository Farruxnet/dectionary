from django.shortcuts import render, HttpResponse
import telebot
from django.conf import settings
bot = telebot.TeleBot(settings.TOKEN)

def web_hook(request):
    if request.method == "POST":
        bot.process_new_updates([telebot.types.Update.de_json(request.body.decode('utf-8'))])
        return HttpResponse(status=200)
    s = '<a href="https://api.telegram.org/bot{0}/setWebhook?url={1}/bot/">WEB</a>'.format(settings.TOKEN, settings.WEB_HOOK_URL)
    return HttpResponse(s)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, 'Hello world')
