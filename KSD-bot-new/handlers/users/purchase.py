from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.inline.choise_buttons import choice
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text='На продажу у нас есть 2 товара: 5 Яблок и 1 Груша. \n'
                              'Есил ничего не нужно - жмите отмену',
                         reply_markup=choice)