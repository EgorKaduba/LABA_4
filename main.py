from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from config import load_config

config = load_config('.env')
bot_token = config.token  # Сохраняем токен в переменную bot_token

bot = Bot(token=bot_token)
dp = Dispatcher()

inline_keyboar = InlineKeyboardMarkup(
    inline_keyboard=[]
)


@dp.message(Command(commands='start'))
async def start(message: Message):
    start_btn = InlineKeyboardButton(text="Начать игру", callback_data="Начать игру")
    inline_keyboar.inline_keyboard.append([start_btn])
    await message.answer("Привет!\nЯ - КвизБот. Нажми на кнопку 'Начать играть', чтобы сыграть со мной в квиз!",
                         reply_markup=inline_keyboar)


if __name__ == "__main__":
    dp.run_polling(bot)
