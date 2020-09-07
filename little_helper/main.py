import logging
import config
from raiffeisen import Raiffeisen
from aiogram import Bot, Dispatcher, executor, types


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
raif = Raiffeisen()

# @dp.message_handler()
# async def test(message: types.Message):
#     await message.answer(message.text)
#     print(message.from_user['first_name'], message.text)

@dp.message_handler(commands=['test'])
async def test2(message: types.Message):
    await message.answer('ololo \n тест')

@dp.message_handler(commands=['курс'])
async def exchange(message: types.Message):
    text = '''
    Банк Райфайзен
    
    Курс валют в Онлайн кабинете:
    Доллары:
    покупка {}
    продажа {}
    Евро:
    покупка {}
    продажа {}
    
    Курс валют в Офисах банка:
    Доллары:
    покупка {}
    продажа {}
    Евро:
    покупка {}
    продажа {}
    
    Курс валют в банкоматах банка:
    Доллары:
    покупка {}
    продажа {}
    Евро:
    покупка {}
    продажа {}
    '''.format(raif.online()['dollar_buy'], raif.online()['dollar_sell'],
               raif.online()['euro_buy'], raif.online()['euro_sell'],
               raif.office()['dollar_buy'], raif.online()['dollar_sell'],
               raif.office()['euro_buy'], raif.online()['euro_sell'],
               raif.card()['dollar_buy'], raif.online()['dollar_sell'],
               raif.card()['euro_buy'], raif.online()['euro_sell'])
    await message.answer(text)

executor.start_polling(dp, skip_updates=True)
