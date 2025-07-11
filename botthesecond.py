from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from asyncio import *
from random import *

import os
import dotenv

dotenv.load_dotenv()
BOT_TOKEN: str = os.getenv('BOT_TOKEN')
print(os.getenv('BOT_TOKEN'))

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

user = {
    'in_game': None,
    'secret_number': None, 
    'played_games': 0,
    'loses': 0,
    'wins': 0,
    'points': 0,
    'total_points': 0,
    'cof': 0
}

def getrandom():
    return randint(1, 100)

async def startbutton(message: Message):
    await message.answer('Я бот для выбора рандомного числа и т.д. и т.п. и вообще бла-бла-бла')

async def check_pos(message: Message):
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = getrandom()
        await message.answer('Я выбрал номер. Угадай')
    else:
        await message.answer('Ты уже в игре')

async def check_neg(message: Message):
    if not user['in_game']:
        await message.answer('Ты не в игре')
    else:
        await message.answer('Ты уже в игре')

async def proans(message: Message):
    if user['in_game']:
        if int(message.text) == int(user['secret_number']):
            user['in_game'] = False
            user['played_games'] += 1
            user['wins'] += 1
            user['total_points'] += user['points']
            user['points'] = 0
            user['cof'] = user['wins'] / user['loses']
            await message.answer('Ты победил')
        if int(message.text) > int(user['secret_number']):
            await message.answer('Меньше')
            user['loses'] += 1
            if user['points'] <= 0:
                user['points'] -= 0
            else:
                user['points'] -= 1
        if int(message.text) < int(user['secret_number']):
            await message.answer('Больше')
            user['loses'] += 1
            if user['points'] <= 0:
                user['points'] -= 0
            else:
                user['points'] -= 1
    else:
        await message.answer('Я выбрал номер. Угадай')

statper = 'Статистика: Сыграно игр:', str(user['played_games']) + ', Побед:', str(user['wins']) + ', Поражений:', str(user['loses']) + ', Коэфицент побед:', str(user['cof']) + ', Очки:', str(user['total_points'])

async def stat(message: Message):
    await message.answer(text = str(statper))

dp.message.register(startbutton, Command(commands=['start']))
dp.message.register(check_pos, F.text.lower().in_(['да', 'ладно', 'давай', 'ок']))
dp.message.register(check_neg, F.text.lower().in_(['нет', 'не', 'не надо', 'нет']))
dp.message.register(proans, lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
dp.message.register(stat, F.text.lower().in_(['статистика']))

async def main():
    print('Бот стартовал')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    run(main())