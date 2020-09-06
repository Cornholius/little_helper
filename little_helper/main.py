import config
import logging
from aiogram import Bot, Dispatcher, executor, types


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler()
# async def test(message: types.Message):
#     await message.answer(message.text)
#     print(message.from_user['first_name'], message.text)

@dp.message_handler(commands=['test'])
async def test2(message: types.Message):
    await message.answer('ololo \n тест')


executor.start_polling(dp, skip_updates=True)
