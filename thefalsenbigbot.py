from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ContentType, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from asyncio import *
from random import *

import os
import dotenv

dotenv.load_dotenv()
BOT_TOKEN: str = os.getenv('BOT_TOKEN')
print(os.getenv('BOT_TOKEN'))

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

#@dp.message(F.text)
#async def inline


but6 = InlineKeyboardButton(text='Press the button',
                            url='https:\youtube.com')
keyb = InlineKeyboardMarkup(inline_keyboard=[[but6]])

async def setmenu(bot: Bot):
    commands_menu = [
        BotCommand(command='/help', description='Помощь'),
        BotCommand(command='/stat', description='Статистика')
    ]
    await bot.set_my_commands(commands_menu)

dp.startup.register(setmenu)

but1 = KeyboardButton(text='кнопка 1')
but2 = KeyboardButton(text='кнопка 2')
but3 = KeyboardButton(text='кнопка 3')
but4 = KeyboardButton(text='кнопка 4')
but5 = KeyboardButton(text='кнопка 5')


keyboard = ReplyKeyboardMarkup(keyboard=[[but1, but2], [but3], [but4, but5]], resize_keyboard=True, one_time_keyboard=True)

@dp.message(CommandStart())
async def start_process(message: Message):
    await message.answer(
        text='hi',
        reply_markup=keyboard
    )

@dp.message(F.text == 'кнопка 3')
async def process_button(message: Message):
    await message.answer(
        text = 'OK',
        reply_markup=ReplyKeyboardRemove()
    )

async def main():
    print('Бот стартовал')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    run(main())