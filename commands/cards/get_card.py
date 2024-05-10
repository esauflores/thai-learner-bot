# This command allows users to retrieve a specific flashcard from the Flashcards project by its English phrase.

# Syntax:

# /get_card <English_phrase>

# Parameters:

# <English_phrase>: The English phrase or word of the flashcard to be retrieved.
# Example:

# /get_card Hello

from telegram import Update, ReplyKeyboardMarkup
from helpers.global_storage import get_storage
from helpers.cards_storage import Card


async def get_card(update: Update, context):
    # Parse the command arguments
    args = context.args
    if len(args) < 1:
        await update.message.reply_text(
            "Invalid command. Please provide the English phrase of the flashcard."
        )
        return

    english_phrase = args[0]

    # Get the storage

    storage = get_storage()

    # Check if the card exists
    card = storage.get_card_by_english_phrase(english_phrase)
    if card is None:
        await update.message.reply_text(
            "Card not found. Please provide a valid English phrase."
        )
        return

    reply = f"Flashcard found:\n{card} \n"
    reply += f"English phrase: {card.english_phrase}\n"
    reply += f"Current Thai translation: {card.thai_translation}\n"
    reply += f"Current tags: {', '.join(card.tags) if card.tags else 'None'}\n"

    markup = ReplyKeyboardMarkup([["Update", "Cancel"]])

    context.user_data["card"] = card

    await update.message.reply_text(reply, reply_markup=markup)
