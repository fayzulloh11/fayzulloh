from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
import logging
from buttons  import natija,natijaa

logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {ism}. Botimizga xush kelibsiz.",reply_markup=natija)

@dp.message_handler(text=["Ma'lumot"])
async def start(message: types.Message):
    await message.answer_photo("https://t.me/alisher_sadullaev/3419",
    caption="Ko'proq Ma'lumot:'https://ezguamal.org/taskin'")

@dp.message_handler(text="Xodimlar haqida ma'lumot")
async def start(message: types.Message):
    await message.answer("🤵🏼 Mamayusupov Ilxom Ravshanovich: Vrach reanimatolog, Bo'lim mudiri",reply_markup=natija)
    await message.answer("🧑 Ochilova Zilola Absalom qizi: Psixolog",reply_markup=natija)




   



if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
