# class storage
# each card has a unique <English_phrase>
# each card has a unique <Thai_translation>
# each card has multiple <tags>, possibly empty


class Card:
    def __init__(self, english_phrase, thai_translation, tags):
        self.english_phrase: str = english_phrase
        self.thai_translation: str = thai_translation
        self.tags: list[str] = tags

    def __str__(self):
        return f"{self.english_phrase} - {self.thai_translation}"

    def __repr__(self):
        return f"{self.english_phrase} - {self.thai_translation}"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False

        return (
            self.english_phrase == other.english_phrase
            and self.thai_translation == other.thai_translation
        )

    def __hash__(self):
        return hash((self.english_phrase, self.thai_translation))

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)

    def has_tag(self, tag):
        return tag in self.tags

    def get_tags(self):
        return self.tags

    def get_english_phrase(self):
        return self.english_phrase

    def get_thai_translation(self):
        return self.thai_translation


class CardsStorage:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card) -> None:
        self.cards.append(card)

    def remove_card(self, card) -> None:
        self.cards.remove(card)

    def get_card_by_english_phrase(self, english_phrase) -> Card | None:
        for card in self.cards:
            if card.get_english_phrase() == english_phrase:
                return card
        return None

    def get_all_cards(self) -> list[Card]:
        return self.cards

    def get_all_cards_with_tags(self, tags) -> list[Card]:
        return [
            card for card in self.cards if any(tag in card.get_tags() for tag in tags)
        ]
