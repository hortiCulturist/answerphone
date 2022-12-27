from pyrogram import Client, filters
from pyrogram.types import Message

import config
import db
from config import api_id, api_hash

db.start_db()
bot = Client("account", api_id, api_hash)
print("RUN")


@bot.on_message(filters.user(config.ADMIN))
def save_text(_, message: Message):
    db.add_message(message.id, message.chat.id)
    bot.send_message(chat_id=message.from_user.id, text='Вы установили текст приветственного сообщения:')
    bot.copy_message(chat_id=message.chat.id, from_chat_id=db.select_message()[1],
                     message_id=db.select_message()[0])


@bot.on_message(filters.all & filters.incoming)
def auto_answer_text(_, message: Message):
    if message.chat.type != message.chat.type.PRIVATE:
        return
    if message.from_user.id in db.all_user():
        return

    db.add_user_db(message.from_user.id)
    bot.copy_message(chat_id=message.chat.id, from_chat_id=db.select_message()[1],
                     message_id=db.select_message()[0])


if __name__ == '__main__':
    bot.run()