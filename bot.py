import asyncio
from config_reader import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandObject

async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    owner = config.owner

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
