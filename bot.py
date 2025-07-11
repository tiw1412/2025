from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
import asyncio

import os
import dotenv

dotenv.load_dotenv()
BOT_TOKEN: str = os.getenv('BOT_TOKEN')
print(os.getenv('BOT_TOKEN'))

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

async def echophoto(message: Message):
    await message.reply_photo(message.photo[0].file_id)
async def echo(message: Message):
    await message.reply(text=message.text)
async def startbutton(message: Message):
    await message.answer('Bluh-bluh-bluh')
async def echostick(message: Message):
    await message.answer_sticker(message.sticker.file_id)
async def echovidnote(message: Message):
    await message.answer_video_note(message.video_note.file_id)

dp.message.register(startbutton, Command(commands=['start']))
dp.message.register(echophoto, F.photo)
dp.message.register(echostick, F.sticker)
dp.message.register(echovidnote, F.video_note)



dp.message.register(echo)

async def main():
    print('Бот стартовал')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())