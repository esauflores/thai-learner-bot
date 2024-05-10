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

queue = []
storage = get_storage()
queue = storage.cards[:]
random.shuffle(queue)

async def start_quizz(update: Update, context: CallbackContext):
    print("hi")
    return ASK_QUESTION

async def ask(update: Update, context: CallbackContext):
    print(queue)
    if queue:  # If there are still questions in the queue
        card = queue[0] # Get the first question from the queue
        await update.message.reply_text(
            f"English phrase: {card.english_phrase}\nPlease provide the Thai translation."
        )
        return CHECK_ANSWER  # Transition to checking the answer
    else:
        await update.message.reply_text("Quiz completed!")  # Notify the user if all questions have been asked
        return ConversationHandler.END  # End the conversation


async def check_answer(update: Update, context: CallbackContext):
    user_response = update.message.text.strip().lower()
    card = queue[0]
    if user_response == card.thai_translation.lower():
        await update.message.reply_text("Correct!")
    else:
        queue.append(queue.pop(0))  # Put the current question back in the queue
        await update.message.reply_text("Wrong answer. Try again.")

    return CONTINUE  # Continue to ask the next question

async def continue_quiz(update: Update, context: CallbackContext):
    user_response = update.message.text.lower()

    if user_response == "yes":
        return ASK_QUESTION  # If the user wants to continue, ask the next question
    elif user_response == "no":
        update.message.reply_text("Quiz stopped.")
        return ConversationHandler.END
    else:
        update.message.reply_text("Please answer with 'yes' or 'no'.")
        return CONTINUE



async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text("Quiz cancelled.")
    return ConversationHandler.END


def main():
    # Create the ConversationHandler for the quiz
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start_quizz', start_quizz)],
        states={
            ASK_QUESTION: [MessageHandler(filters.TEXT, ask)],
            CHECK_ANSWER: [MessageHandler(filters.TEXT, check_answer)],
            CONTINUE: [MessageHandler(filters.TEXT, continue_quiz)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    return conv_handler
