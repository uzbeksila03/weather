from aiogram import types
from loader import bot


async def set_default_commands():
    await bot.set_my_commands(
        [
            types.bot_command.BotCommand(command="start", description="Botni ishga tushurish"),
            types.bot_command.BotCommand(command="help", description="Yordam"),
            types.bot_command.BotCommand(command="bugun", description="Bugungi kunlik ob-havo"),
            types.bot_command.BotCommand(command="ertaga", description="Ertangi kunlik ob-havo"),
            types.bot_command.BotCommand(command="haftalik", description="Haftalik ob-havo"),

        ]
    )
