from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


info = KeyboardButton(text="Ma'lumot")
xodimlar = KeyboardButton(text="Xodimlar haqida ma'lumot")
yordam = KeyboardButton(text="nima yordam bera olaman")
savol = KeyboardButton(text="savollar")
til = KeyboardButton(text="tilni ozgartirish")

bolim_mudiri = KeyboardButton(text="bolim mudiri")
shifokor = KeyboardButton(text="shifokor")
psixolog = KeyboardButton(text="psixolog")
shifokor = KeyboardButton(text="👩‍⚕️ Yusupova Muyassar: Hamshira")
ijtimoiy_xodim = KeyboardButton(text="ijtimoiy xodim")



natijaa = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(bolim_mudiri,shifokor).row(psixolog,ijtimoiy_xodim)

natija = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(info).add(xodimlar).add(yordam).add(savol,til)

ingiliz = KeyboardButton(text="ingiliz tili")
turk = KeyboardButton(text="turk tili")
rus = KeyboardButton(text="rus tili")
ozbek = KeyboardButton(text="ozbek tili")
til = KeyboardButton(text="tilni ozgartirish")