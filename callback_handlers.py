import subprocess
import os
import time
import threading
import keyboards
import texts
import sys
import mouse_walk
import asyncio

from aiogram import Router
from aiogram import F
from aiogram.types.message import Message
from aiogram.types.callback_query import CallbackQuery
from aiogram.types import FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from settings import Settings
from playsound import playsound

router = Router()

class NotificationState(StatesGroup):
    user_text = State()


@router.callback_query(F.data == "collapse_windows")
async def collapse_windows(clb: CallbackQuery):
    try:
        subprocess.run("powershell -command (New-Object -ComObject Shell.Application).MinimizeAll()")
        await clb.answer("Окна свернуты")
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "turn_off_pc")
async def turn_off_pc(clb: CallbackQuery):
    await clb.answer()
    await clb.message.reply("Выключить пк:", reply_markup=await keyboards.get_turn_off_pc_keyboard())

@router.callback_query(F.data == "sleep_pc")
async def sleep_pc(clb: CallbackQuery):
    await clb.answer()
    try:
        await clb.message.edit_text(text="<b>Компьютер во сне</b>")
        os.system("shutdown /h")
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "shutdown_pc")
async def shutdown_pc(clb: CallbackQuery):
    await clb.answer()
    try:
        await clb.message.edit_text(text="<b>Компьютер завершил работу</b>")
        os.system("shutdown /s /t 1")
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "cancel")
async def cancel(clb: CallbackQuery):
    await clb.answer()
    try:
        await clb.message.delete()
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "screenshot")
async def screenshot(clb: CallbackQuery):
    await clb.answer()
    try:
        settings = Settings()
        current_directory = os.getcwd()
        nircmd_path = current_directory + "\\nircmd.exe"
        screenshot_name = str(time.time()).replace(".", "") + ".png"
        screenshot_filename = current_directory + "\\screenshots\\" + screenshot_name
        subprocess.run(f'"{nircmd_path}" savescreenshot "{screenshot_filename}"', shell=False)
        img = FSInputFile(screenshot_filename)
        if settings.get_screenshots_quality(raw_data=True) == "hight":
            await clb.message.reply_document(img)
        elif settings.get_screenshots_quality(raw_data=True) == "low":
            await clb.message.reply_photo(img)
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "notification")
async def notification(clb: CallbackQuery, state: FSMContext):
    await clb.answer()
    try:
        await clb.message.answer("Отправьте текст уведомления:")
        await state.set_state(NotificationState.user_text)
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.message(NotificationState.user_text)
async def send_notification(msg: Message, state: FSMContext):
    user_text = msg.text
    current_directory = os.getcwd()
    nircmd_path = current_directory + "\\nircmd.exe"
    def show_notification():
        subprocess.run(f'"{nircmd_path}" infobox "{user_text}" "Вам послание!"')
    thread = threading.Thread(target=show_notification)
    thread.start()
    await msg.reply("<b>Сообщение отправлено</b>")

@router.callback_query(F.data == "turn_off_monitor")
async def turn_off_monitor(clb: CallbackQuery):
    try:
        current_directory = os.getcwd()
        nircmd_path = current_directory + "\\nircmd.exe"
        proc = subprocess.Popen(f'"{nircmd_path}" monitor off')
        await clb.answer("Монитор потух")
        await asyncio.sleep(2)
        proc.kill()  # процесс NirCmd почему-то сам не завершается, поэтому я закрываю его вручную спустя 2 секунды
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "turn_off_volume")
async def turn_off_volume(clb: CallbackQuery):
    try:
        current_directory = os.getcwd()
        nircmd_path = current_directory + "\\nircmd.exe"
        subprocess.run(f'"{nircmd_path}" mutesysvolume 1')
        await clb.answer("Звук выключен")
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "set_screenshots_quality")
async def set_screenshots_quality(clb: CallbackQuery):
    await clb.answer()
    try:
        settings = Settings()
        settings.set_screenshots_quality()
        await clb.message.edit_text(texts.get_settings_text(), reply_markup=await keyboards.get_settings_keyboard())
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "set_start_notification")
async def set_start_notification(clb: CallbackQuery):
    await clb.answer()
    try:
        settings = Settings()
        settings.set_start_notification()
        await clb.message.edit_text(texts.get_settings_text(), reply_markup=await keyboards.get_settings_keyboard())
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "clear_screenshots")
async def clear_screenshots(clb: CallbackQuery):
    try:
        screenshots_path = os.getcwd() + "\\screenshots\\"
        for img in os.listdir(screenshots_path):
            os.remove(screenshots_path + img)
        await clb.answer("Скриншоты удалены")
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "turn_off_bot")
async def turn_off_bot(clb: CallbackQuery):
    await clb.answer()
    try:
        await clb.message.reply("<b>Бот выключен</b>")
        sys.exit()
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "sound")
async def sound(clb: CallbackQuery):
    try:
        def play_sound():
            playsound("hi-hi-hi-ha-clash-royale.mp3")
        thread = threading.Thread(target=play_sound)
        thread.start()
        await clb.answer("Хи-хи-ха-ха")
    except Exception as ex:
        await clb.message.reply(text=ex)

@router.callback_query(F.data == "mouse_dance")
async def mouse_dance(clb: CallbackQuery):
    try:
        def start_mouse_dance():
            mouse_walk.start_mouse_walk(4)
        thread = threading.Thread(target=start_mouse_dance)
        thread.start()
        await clb.answer("Мышь танцует")
    except Exception as ex:
        await clb.message.reply(text=ex)
