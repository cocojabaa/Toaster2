import keyboards
import texts

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types.message import Message
from aiogram import types

from random import randint

router = Router()


@router.message(Command("start"))
async def start(msg: Message):
    try:
        await msg.reply("==🖥️  Управление компьютером  🖥️==", reply_markup=await keyboards.get_main_keyboard())
    except Exception as ex:
        await msg.reply(text=ex)

@router.message(Command("test"))
async def test(msg: Message):
    try:
        stickers = texts.stickers
        random_sticker_id = randint(0, len(stickers) - 1)
        await msg.answer_sticker(sticker=stickers[random_sticker_id], reply_markup=types.ReplyKeyboardRemove())

    except Exception as ex:
        await msg.reply(text=ex)

@router.message(Command("settings"))
async def settings(msg: Message):
    try:
        await msg.reply(texts.get_settings_text(), reply_markup=await keyboards.get_settings_keyboard())
    except Exception as ex:
        await msg.reply(text=ex)
