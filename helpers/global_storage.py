import helpers.cards_storage as cards_storage

storage = {}


def get_storage():
    global storage

    if not storage:
        storage = cards_storage.CardsStorage()

    return storage
