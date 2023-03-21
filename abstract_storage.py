from abc import ABC

# класс "Пример"
class Storage(ABC):
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def add(self, title, quantity) -> None:
        pass

    def remove(self, title, quantity) -> None:
        pass

    def get_free_space(self) -> int:
        pass

    def get_items(self):
        pass

    def unique_items_count(self):
        pass
