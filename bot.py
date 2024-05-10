from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from helpers.env import get_env_variable

from commands.cards.add_card import add_card
from commands.cards.update_card import update_card
from commands.cards.get_card import get_card
from commands.quizz import start_quizz


def main():
    bot_token = get_env_variable("BOT_TOKEN")

    print("Bot is running...")

    app = Application.builder().token(bot_token).build()

    app.add_handler(start_quizz.main())

    app.add_handler(
        CommandHandler(command="add_card", callback=add_card, has_args=True),
    )

    app.add_handler(
        CommandHandler(command="update_card", callback=update_card, has_args=True),
    )

    app.add_handler(
        CommandHandler(command="get_card", callback=get_card, has_args=True),
    )

    app.run_polling()


if __name__ == "__main__":
    main()
