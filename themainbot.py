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

 ##   ##                    ###        ##                                                             ##
 ##   ##                     ##                                                                       ##
 ##   ##   ####    ######    ##  ##   ###     #####     ### ##           ######    ####    ######    #####
 ## # ##  ##  ##    ##  ##   ## ##     ##     ##  ##   ##  ##             ##  ##      ##    ##  ##    ##
 #######  ##  ##    ##       ####      ##     ##  ##   ##  ##             ##  ##   #####    ##        ##
 ### ###  ##  ##    ##       ## ##     ##     ##  ##    #####             #####   ##  ##    ##        ## ##
 ##   ##   ####    ####      ##  ##   ####    ##  ##       ##             ##       #####   ####        ###
                                                       #####             ####
alldata = {
    'uwtptg': None,
    'step': 0,
    'prevstep': 0
}
step = alldata['step']
prevstep = alldata['prevstep']
allbut = {
    'farmerstory': {
        'start': [KeyboardButton(text='История про фермера')],
        'part1': [
                KeyboardButton(text='Холодный'),
                KeyboardButton(text='Умерненный'),
                KeyboardButton(text='Жаркий')
        ]
    }
}
fs = allbut['farmerstory']
allkeybs = {
    'farmerstory': {
        'start': ReplyKeyboardMarkup(keyboard=[fs['start']], resize_keyboard=True, one_time_keyboard=True),
        'part1': {
            'kbs1': ReplyKeyboardMarkup(keyboard=[fs['part1']], resize_keyboard=True, one_time_keyboard=True),
        }
    }
}
fsk = allkeybs['farmerstory']

def addstep(step):
    step += 1
    return(step)

async def stepchcker():
    if not prevstep == step:
        async def mainneg(message: Message):
            await message.answer('Нельзя отойти на шаг назад ⌛')        
    
 ##   ##             ##                                                    ##
 ### ###                                                                   ##
 #######   ####     ###     #####             ######    ####    ######    #####
 #######      ##     ##     ##  ##             ##  ##      ##    ##  ##    ##
 ## # ##   #####     ##     ##  ##             ##  ##   #####    ##        ##
 ##   ##  ##  ##     ##     ##  ##             #####   ##  ##    ##        ## ##
 ##   ##   #####    ####    ##  ##             ##       #####   ####        ###
                                              ####



async def startbutton(message: Message):
    await message.answer('Здравствуй! 👋. Я супер-пупер-мега-ультра-глобально-абсолютно-лучший-путевдодитель-рассказчикисторий-бот, который может рассказать увлекательные истории на любой вкус, цвет, запах и много чего еще. Но есть один вопрос. Хочешь ли ты?')

async def playthegame(message: Message):
    if not alldata['uwtptg']:
        await message.answer('Отлично! Вот тебе истории на выбор: 📖🖋 (Пока что готова (и то не полностью) только одна)',
                             reply_markup= fsk['start'])
        alldata['uwtptg'] = True
        reply_markup= fsk['start']
    else:
        await message.answer('Нельзя начать новую историю, не закончив уже идущую ❌🔚')
async def dontplay(message: Message):
    if not alldata['uwtptg']:
        await message.answer('Хорошо. Но как захочешь, просто напиши "Хочу сыграть". Пока! 👋')
        reply_markup=ReplyKeyboardRemove()
    else:
        await message.answer('Нельзя начать новую историю, не закончив уже идущую ❌🔚')

@dp.message(F.text == 'История про фермера')
async def process_button(message: Message):
    await message.answer(
        text = 'Отлично!\n' \
        '----------\n' \
        'Итак, вы фермер. Ну еще не совсем, но все же. 👨‍🌾\n' \
        'Маленькая предыстория: Совсем недавно, около 2-х недель назад, вы были атакованы судьбой: страшный пожар, который был вызван абсолютной случайностью, перекинулся на ваш дом. Однако, никто, вообще никто, не помог вам. В итоге все сгорело еще задолго до приезда пожарных. Окончательно разочаровавшись в людях, вы решили купить маленький участок, где-то в глуши. Главное подальше от общества. 😱 У вас есть три участка на выбор:\n'
        '1-й: Холодный климат, но навряд ли кто-то из людей захочет соваться в такую глушь. Животным будет вообще все равно, но вот растениям - туго ❄\n' \
        '2-й: Умеренный климат. И животным, и растениям будет очень хорошо, но люди будут заходить к вам часто. (Советую брать этот вариант) 🌲\n' \
        '3-й: Жаркий климат. Люди будут заходить к вам, но реже, чем на умеренном климате, однако животным будет не очень хорошо, в отличии от растений ☀\n',
        reply_markup=fsk['part1']['kbs1'],
        prevstep = 1,
        step = addstep(step)
    )

 #####
  ## ##
  ##  ##  ######    ####     #####
  ##  ##   ##  ##  ##  ##   ##
  ##  ##   ##  ##  ######    #####
  ## ##    #####   ##            ##
 #####     ##       #####   ######
          ####

dp.message.register(dontplay, F.text.lower().in_(['нет', 'не', 'не надо', 'нет']))
dp.message.register(startbutton, Command(commands=['start']))
dp.message.register(playthegame, F.text.lower().in_(['да', 'давай', 'ок', 'хорошо', 'хочу сыграть']))

    ##       ##    ######                              ###         ##       ##
    ##       ##    # ## #                               ##         ##       ##
   ##       ##       ##     ######    ####     #####    ##        ##       ##
                     ##      ##  ##      ##   ##        #####
                     ##      ##       #####    #####    ##  ##
                     ##      ##      ##  ##        ##   ##  ##
                    ####    ####      #####   ######   ###  ##

async def main():
    print('Бот стартовал')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    run(main())