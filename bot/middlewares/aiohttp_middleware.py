from aiohttp import ClientSession
from aiogram.types import Update, TelegramObject
from aiogram.dispatcher.middlewares.base import BaseMiddleware

class AiohttpSessionMiddleware(BaseMiddleware):
    def __init__(self, session: ClientSession):
        self.session = session
        super().__init__()

    async def __call__(self, handler, event: Update, data: dict):
        data["session"] = self.session  # Передаємо сесію у кожен хендлер
        return await handler(event, data)
    
class BotMiddleware(BaseMiddleware):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    async def __call__(self, handler, event: TelegramObject, data: dict):
        # Передаємо бота в контекст
        data["bot"] = self.bot
        return await handler(event, data)