import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor
import csv, datetime, sqlite3

API_TOKEN = '2044977588:AAE-n8xQGfV9EdlevkiaCrdEWS5yfQcaUEo'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply("Holla amigo or chika!")
    statistics(message.chat.id, message.text)
    stat(message.chat.id, message.text)

def stat(user_id, command):
    sqlite_connection = sqlite3.connect('bot.db')
    cursor = sqlite_connection.cursor()
    data = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO stat(user_id, user_command, date) VALUES('%s','%s','%s')" % (user_id, command, data))
    sqlite_connection.commit()
    cursor.close()


    
def statistics(user_id, command):
    data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
    with open('data.csv', 'a', newline="") as fil:
        wr = csv.writer(fil, delimiter=';')
        wr.writerow([data, user_id, command])

if __name__ == '__main__':
    executor.start_polling(dp)
