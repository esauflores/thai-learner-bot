import random
from telegram import Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
    CallbackContext,
)

from helpers.global_storage import get_storage

# Define states
ASK_QUESTION, CHECK_ANSWER, CONTINUE = range(3)


async def start_quizz(update: Update, context: CallbackContext):
    global queue
    storage = get_storage()
    queue = storage.cards[:]
    random.shuffle(queue)

    # clear user data

    print("Start quizz")

    await update.message.reply_text("Start quizz.")
    return await ask(update, context, queue)  # Await the result of ask()


async def ask(update: Update, context: CallbackContext, queue):

    card = queue[0]  # Get the first question from the queue
    await update.message.reply_text(
        f"English phrase: {card.english_phrase}\nPlease provide the Thai translation."
    )
    return CHECK_ANSWER  # Transition to checking the answer


async def check_answer(update: Update, context: CallbackContext):
    user_response = update.message.text.strip().lower()
    card = queue[0]
    if user_response == card.thai_translation.lower():
        queue.pop(0)
        if len(queue) > 0:
            await update.message.reply_text(
                "Correct! \n Do you want to continue quizz? (yes/no)"
            )

        else:
            await update.message.reply_text("Correct! \n Quiz completed!")
            return ConversationHandler.END
    else:
        queue.append(queue.pop(0))  # Put the current question back in the que

        await update.message.reply_text(
            "Wrong answer. The answer is: "
            + card.thai_translation
            + "\nDo you want to continue quizz? (yes/no)"
        )
    return CONTINUE


async def continue_quiz(update: Update, context: CallbackContext):
    user_response = update.message.text.lower()

    if user_response == "yes":
        return await ask(update, context, queue)  # Await the result of ask()
    elif user_response == "no":
        await update.message.reply_text("Quiz stopped.")
        return ConversationHandler.END
    else:
        await update.message.reply_text("Please answer with 'yes' or 'no'.")
        return CONTINUE


async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text("Quiz cancelled.")
    return ConversationHandler.END


def main():
    # Create the ConversationHandler for the quiz
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start_quizz", start_quizz)],
        states={
            CHECK_ANSWER: [MessageHandler(filters.TEXT, check_answer)],
            CONTINUE: [MessageHandler(filters.TEXT, continue_quiz)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    return conv_handler
