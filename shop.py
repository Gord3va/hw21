from storage import BaseStorage
from exceptions import TooManyDifferentProducts


class Shop(BaseStorage):

    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, title, quantity) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts

        super().add(title, quantity)
