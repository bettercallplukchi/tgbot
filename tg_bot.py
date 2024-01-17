from telebot import types
import telebot

token = "6639037739:AAEy5MPArzVmdrvFC9HyX_oRwLrr-dnbsgM"
bot = telebot.TeleBot(token)
my_chat_id = 5754285878


@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="О нас")
    button_geo = types.KeyboardButton(text="Услуги")
    button3 = types.KeyboardButton(text="Оставить заявку")
    keyboard.add(button_phone, button_geo, button3)
    bot.send_message(
        message.chat.id,
        "Вас приветствует, компания дизайна WALTER",
        reply_markup=keyboard,
    )


def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(
        text="О нас", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )
    keyboard.add(url_button)
    bot.send_message(
        message.chat.id,
        "Для ознакомления с более подробной информацией, перейдите по ссылке",
        reply_markup=keyboard,
    )


def sent_request(message):
    mes = f"Новая заявка: {message.text}"
    bot.send_message(my_chat_id, mes)
    bot.send_message(
        message.chat.id,
        "Спасибо за заявку, вскоре заявка будет обработана и с вами свяжутся!",
    )


def send_service(message):
    bot.send_message(message.chat.id, "1. Сделать лэндинг")
    bot.send_message(message.chat.id, "2. Сделать полную веб-разработку")
    bot.send_message(message.chat.id, "3. Сайт с вёрсткой")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text.lower() == "о нас":
        info_func(message)
    elif message.text.lower() == "оставить заявку":
        bot.send_message(
            message.chat.id, "Будем рады вас обслужить! Оставьте контактные данные."
        )
        bot.register_next_step_handler(message, sent_request)
    elif message.text.lower() == "услуги":
        send_service(message)
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
