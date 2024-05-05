import base_handlers
import callback_handlers
import asyncio
import os

from aiogram import Dispatcher, Bot
from aiogram.methods import DeleteWebhook
from dotenv import load_dotenv

import colorama


dp = Dispatcher()

load_dotenv()

async def main():
    bot = Bot(os.getenv("TOKEN"), parse_mode="HTML")

    dp = Dispatcher()
    dp.include_routers(base_handlers.router, callback_handlers.router)

    await bot(DeleteWebhook(drop_pending_updates=True))  # Пропускать обновления
    await dp.start_polling(bot)

if __name__ == "__main__":
    colorama.init()
    print(f"{'='*20} " + colorama.Fore.GREEN + "Bot was started" + colorama.Style.RESET_ALL + f" {'='*20}")
    asyncio.run(main())
