from telegram import Update, ReplyKeyboardRemove
from helpers.global_storage import get_storage
from helpers.cards_storage import Card


# This command allows users to update an existing flashcard in the Flashcards project.

# Syntax:

# /update_card <English_phrase> <New_Thai_translation> [tags]

# Parameters:

# <English_phrase>: The English phrase or word of the flashcard to be updated.
# <New_Thai_translation>: The new Thai translation for the flashcard.
# [tags] (optional): Any new tags to be associated with the flashcard. Multiple tags can be provided, separated by spaces.
# Example:

# /update_card Hello สวัสดี Greeting Vocabulary


async def update_card(update: Update, context):
    # Parse the command arguments
    args = context.args
    if len(args) < 2:
        await update.message.reply_text(
            "Invalid command. Please provide the English phrase and the new Thai translation."
        )
        return

    # get the storage

    storage = get_storage()

    # Check if the card exists
    card = storage.get_card_by_english_phrase(args[0])

    if card is None:
        await update.message.reply_text(
            "Card not found. Please provide a valid English phrase."
        )
        return

    # Update the card with the new Thai translation and tags
    card.thai_translation = args[1]
    card.tags = args[2:] if len(args) > 2 else []

    await update.message.reply_text(
        "Flashcard updated successfully.", reply_markup=ReplyKeyboardRemove()
    )
