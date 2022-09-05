import telebot
from config import token, keys

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты>\<в какую валюту перевести>\<количество переводимой валюты>\<Чтобы увидеть список доступных валют: /values >'
    bot.reply_to(message, text)
bot.polling()
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
   values = message.text.split (' ')

   if lem(values) > 3:
       raise ConvertionException('Слишком много параметров.')
   quote, base, amount = values
   r = requests.get (f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
   total_base = json.loads(r.content)[keye[base]]
   text = f'Цена {amount} {quote} в  {base} - {total_base}'
   bot.send_messanga(message.chat.id,text)
   bot.polling()