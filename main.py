from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, BotCommand

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


@dp.message(Command(commands='contacts'))
async def contacts(message: Message):
    await message.answer("Электронная почта: egor.kaduba@mail.ru\nТелеграмм: @sTeNki_ok")


@dp.message(Command(commands='help'))
async def bot_help(message: Message):
    await message.answer("Пока тут ничего нет, но скоро появится")


async def set_main_menu():
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
    ]

    await bot.set_my_commands(main_menu_commands)


dp.startup.register(set_main_menu)
if __name__ == "__main__":
    dp.run_polling(bot)
