# This helper function is used to get a random set of flashcards from the Flashcards project.


import random
from typing import Optional
from helpers.global_storage import get_storage
from helpers.cards_storage import Card


# Get a random set of flashcards from the Flashcards project
# count: The number of flashcards to retrieve
# tags: Optional tags used to filter the flashcards


def get_random_cards(*, count: int = 1, tags: Optional[list[str]] = None) -> list[Card]:
    storage = get_storage()

    if tags:
        cards = storage.get_cards_by_tags(tags)
    else:
        cards = storage.get_all_cards()

    if count > len(cards):
        return Exception("Not enough cards available.")

    return random.sample(cards, count)
