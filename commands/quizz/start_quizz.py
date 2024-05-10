# This command allows users to start a quiz session using flashcards from the Flashcards project.

# Syntax:

# /start_quizz [tags]
# Parameters:

# [tags] (optional): Tags used to filter flashcards for the quiz. If provided, only flashcards with matching tags will be included in the quiz. If not provided, flashcards from all tags will be included.
# Example:

# /start_quizz Greeting Vocabulary
# /start_quizz

import random
from telegram import Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)

from helpers.global_storage import get_storage

queue = []


async def start_quizz(update: Update, context: CallbackContext):
    global queue

    storage = get_storage()
    queue = storage.cards[:]
    random.shuffle(queue)

    # Start presenting questions
    for card in queue:
        await update.message.reply_text(
            f"English phrase: {card.english_phrase}\nPlease provide the Thai translation."
        )
        user_response = None
        while user_response is None:
            updates = await context.bot.get_updates(update.update_id + 1)
            print(updates)
            # Check for new messages in the update object
            for u in updates:
                if u.message and u.message.text and not u.message.text.startswith("/"):
                    user_response = u.message.text

        if card.thai_translation == user_response:

            queue.pop(0)  # Remove the current question from the queue

            await update.message.reply_text(
                "Correct! Let's get the next English phrase."
            )

        else:
            # Move the current question to the end of the queue
            queue.append(queue.pop(0))
            await update.message.reply_text(
                "Wrong answer. Let's get the next English phrase."
            )

    await update.message.reply_text("Quiz completed!")
    return
