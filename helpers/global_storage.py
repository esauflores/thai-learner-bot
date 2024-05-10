from helpers.cards_storage import Card, CardsStorage as cards_storage

storage = None


def initialize_storage():
    global storage

    storage.add_card(Card("Hello", "สวัสดี", ["Greeting", "Vocabulary"]))
    storage.add_card(Card("Goodbye", "ลาก่อน", ["Greeting", "Vocabulary"]))
    storage.add_card(Card("Thank you", "ขอบคุณ", ["Vocabulary"]))

    storage.add_card(Card("Cat", "แมว", ["Animal", "Pet"]))
    storage.add_card(Card("Dog", "หมา", ["Animal", "Pet"]))
    storage.add_card(Card("Elephant", "ช้าง", ["Animal"]))


def get_storage():
    global storage

    if not storage:
        storage = cards_storage.CardsStorage()
        initialize_storage()

    return storage
