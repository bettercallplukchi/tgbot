from telebot import types
import telebot

token = "6639037739:AAEy5MPArzVmdrvFC9HyX_oRwLrr-dnbsgM"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_dice(message.chat.id)
    bot.send_message(message.chat.id, "Привет я родился!")


@bot.message_handler(commands=["info"])
def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(
        text="Ссылка на наш сайт", url="https://ya.ru"
    )
    keyboard.add(url_button)
    bot.send_message(
        message.chat.id,
        "Привет! Это мой личный профиль, за информацией обращаться сюда!",
        reply_markup=keyboard,
    )


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
