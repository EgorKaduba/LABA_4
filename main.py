from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, BotCommand, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import load_config
from inline_keyboard import create_inline_kb
from questions_dir import questions_func

config = load_config('.env')
bot_token = config.token  # Сохраняем токен в переменную bot_token

bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(Command(commands='start'))
async def start(message: Message):
    inline_keyboar = create_inline_kb(1, "start_game")
    await message.answer("Привет!👋\nЯ - КвизБот. Нажми на кнопку 'Начать играть', чтобы сыграть со мной в квиз!🎰",
                         reply_markup=inline_keyboar)


@dp.message(Command(commands='contacts'))
async def contacts(message: Message):
    await message.answer("Электронная почта: egor.kaduba@mail.ru\nТелеграмм: @sTeNki_ok")


@dp.message(Command(commands='help'))
async def bot_help(message: Message):
    await message.answer("Пока тут ничего нет, но скоро появится")


@dp.callback_query(F.data.in_('start_game'))
async def start_game(callback: CallbackQuery):
    inline_keyboar = create_inline_kb(3, *questions_func.get_list_category(), last_btn="random_question")
    await callback.message.answer("Выбирай🤔", reply_markup=inline_keyboar)


@dp.callback_query(F.data.in_(["programming", "history", "geography", "art", "science", "random_question"]))
async def chek_q(callback: CallbackQuery):
    if callback.data == "random_question":
        question = questions_func.get_random_question()
    else:
        question = questions_func.get_random_question_category(callback.data)
    inline_keyboard = create_inline_kb(1, *question['варианты'])
    await callback.message.answer(question['вопрос'], reply_markup=inline_keyboard)


@dp.callback_query()
async def answer(callback: CallbackQuery):
    question_text = callback.message.text
    choice = callback.data
    for question in questions_func.get_all_questions():
        if question['вопрос'] == question_text and question:
            if question['варианты'][question['правильный_ответ']] == choice:
                await callback.answer("Верно")
                break
            await callback.answer("Неверно")
            break
    inline_keyword = create_inline_kb(1, 'start_game')
    await callback.message.answer("Сыграем ещё раз?", reply_markup=inline_keyword)


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
