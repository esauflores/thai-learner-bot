from helpers.cards_storage import CardsStorage, Card
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove


# This command allows users to add new flashcards to the Flashcards project, helping them learn English to Thai translations.

# Syntax:

# /add_card <English_phrase> <Thai_translation> [tags]

# Parameters:

# <English_phrase>: The English phrase or word to be translated.
# <Thai_translation>: The corresponding translation in Thai.
# [tags] (optional): Any tags or labels to categorize the flashcard.
# Example:

# /add_card Hello สวัสดี Greeting


async def add_card(update: Update, context, card_storage: CardsStorage):
    # Parse the command arguments
    args = context.args
    if len(args) < 2:
        await update.message.reply_text(
            "Invalid command. Please provide the English phrase and the Thai translation."
        )
        return

    english_phrase = args[0]
    thai_translation = args[1]
    tags = args[2:] if len(args) > 2 else []

    # Check if the card already exists
    if card_storage.get_card_by_english_phrase(english_phrase) is not None:
        await update.message.reply_text(
            "Card already exists. Please provide a different English phrase."
        )
        return

    # Create a new card and add it to the storage
    card = Card(english_phrase, thai_translation, tags)
    card_storage.add_card(card)

    await update.message.reply_text(
        "Flashcard added successfully.", reply_markup=ReplyKeyboardRemove()
    )
