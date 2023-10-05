import os
import logging
from aiogram import Bot, Dispatcher, executor, types

# logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = u'D:/Для общей папки linux/Python/Ver1/mylog.log')
logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = u'./log/mylog.log')

# bot = Bot(token="6386892516:AAEafLw7rUan_Be2mriQ09Xk8IQRQ-lrMBs")
bot = Bot(token = os.getenv("API_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler()
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


