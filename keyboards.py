from aiogram.utils.keyboard import InlineKeyboardBuilder

async def get_main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Свернуть окна", callback_data="collapse_windows")
    builder.button(text="Издать звук", callback_data="sound")
    builder.button(text="Мышиный танец", callback_data="mouse_dance")
    builder.button(text="Скриншот", callback_data="screenshot")
    builder.button(text="Уведомление", callback_data="notification")
    builder.button(text="Убрать звук", callback_data="turn_off_volume")
    builder.button(text="Выкл монитор", callback_data="turn_off_monitor")
    builder.button(text="Выключить пк", callback_data="turn_off_pc")
    builder.adjust(3, 3, 2)
    return builder.as_markup()

async def get_settings_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Качество скриншотов", callback_data="set_screenshots_quality")
    builder.button(text="Очистить скриншоты", callback_data="clear_screenshots")
    builder.button(text="Отключить бота", callback_data="turn_off_bot")
    builder.adjust(2, 1)
    return builder.as_markup()

async def get_turn_off_pc_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="В сон", callback_data="sleep_pc")
    builder.button(text="В завершение", callback_data="shutdown_pc")
    builder.button(text="Отмена", callback_data="cancel")
    builder.adjust(3)
    return builder.as_markup()
