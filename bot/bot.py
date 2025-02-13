from dotenv import load_dotenv
import aiohttp
from aiogram import Bot,Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from hendler import router
# from hendler_menu import router as router_menu
from keyboards import set_bot_commands
from middlewares.aiohttp_middleware import AiohttpSessionMiddleware, BotMiddleware

import asyncio
import os
import logging

load_dotenv()

TOKEN = os.getenv("telegram_token")

bot = Bot(token=TOKEN)
dp = Dispatcher()
session: aiohttp.ClientSession | None = None  # Глобальна змінна для сесії


logging.basicConfig(level=logging.INFO)

dp.include_router(router)
# dp.include_router(router_menu)


# function when start bot
async def on_startup():
    global session
    global bot
    session = aiohttp.ClientSession()  
    dp.update.middleware(AiohttpSessionMiddleware(session))
    dp.update.middleware(BotMiddleware(bot))
    logging.info(f"🔹 ClientSession ID: {id(session)}")
    logging.info(" ClientSession запущено і додано в middleware")

# function when finish bot
async def on_shutdown():
    global session
    if session:
        await session.close()  
        logging.info(" ClientSession Закрито")


async def main():
    await on_startup()
    try:
        await set_bot_commands(bot)
        await dp.start_polling(bot)

    finally:
        await on_shutdown()
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())