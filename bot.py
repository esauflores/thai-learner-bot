from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)
from commands.test import start, default_reply, user_info, help, menu
from helpers.env import get_env_variable
from helpers.cards_storage import CardsStorage

cards_storage = CardsStorage()


def main():
    bot_token = get_env_variable("BOT_TOKEN")

    print("Bot is running...")

    app = Application.builder().token(bot_token).build()
    app.add_handler(CommandHandler(command="start", callback=start))
    app.add_handler(
        MessageHandler(filters=filters.FORWARDED & ~filters.COMMAND, callback=user_info)
    )
    app.add_handler(CommandHandler(command="help", callback=help))
    app.add_handler(CommandHandler(command="menu", callback=menu))

    app.add_handler(MessageHandler(filters=filters.TEXT, callback=default_reply))

    app.run_polling()


if __name__ == "__main__":
    main()
