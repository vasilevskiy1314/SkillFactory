import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CurrencyConvertor


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите через пробел 3 параметра: \
\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \
\nИмена валют должны быть написаны в единственном числе, \
количество переводимой валюты должно быть написано цифрами\
\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException(f'Неверное число параметров!')

        quote, base, amount = values
        cost = CurrencyConvertor.convert(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка ввода пользователя! \n{e} \
\nПомощь: /help'
)

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду! \n{e} \
Помощь: /help '
)

    else:
        text = f'Цена {amount} {quote} в {base} - {cost}'
        bot.reply_to(message, text)

bot.polling()