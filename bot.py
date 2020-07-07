from config import token, actions
from telebot import TeleBot, types
import logging

logger = logging.getLogger('requests')
handler = logging.FileHandler('requests')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.WARNING)

bot = TeleBot(token)
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(*[types.KeyboardButton(_) for _ in actions])


@bot.message_handler()
def start(m):
    request = {
        'name': m.chat.first_name,
        'text': m.text,
        'id': m.chat.id,
    }

    if m.chat.last_name: request['lastname'] = m.chat.last_name
    logger.warning(request)

    answer = actions[m.text]() if m.text in actions else 'Выберите значение из списка'
    bot.send_message(m.chat.id, answer, reply_markup=keyboard)


if __name__ == '__main__':
     bot.polling(none_stop=True)
