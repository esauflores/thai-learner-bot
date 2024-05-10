from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from helpers.env import get_env_variable

from commands.add_card import add_card
from commands.update_card import update_card
from commands.get_card import get_card
from commands.default_reply import default_reply
from commands.start_quizz import start_quizz


from dotenv import load_dotenv

load_dotenv()

def main():
    bot_token = get_env_variable("BOT_TOKEN")

    print("Bot is running...")

    app = Application.builder().token(bot_token).build()
    


    app.add_handler(
        CommandHandler(command="add_card", callback=add_card, has_args=True),
    )

    app.add_handler(
        CommandHandler(command="update_card", callback=update_card, has_args=True),
    )


    app.add_handler(
        CommandHandler(command="get_card", callback=get_card, has_args=True),
    )

    # app.add_handler(CommandHandler(command="update_card", callback=update_card))

    # app.add_handler(CommandHandler(command="get_card", callback=get_card))
    
    app.add_handler(
        CommandHandler(command="start_quizz", callback=start_quizz, has_args=False),
    )

    app.add_handler(
        MessageHandler(filters=filters.TEXT, callback=default_reply)
    )

    app.run_polling()





if __name__ == "__main__":
    main()