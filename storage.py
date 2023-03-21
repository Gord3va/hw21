from abstract_storage import Storage
from exceptions import NotEnoughSpace, NotEnoughProduct

#класс основанный на примере из abstract_storage
class BaseStorage(Storage):
    def __init__(self, items: dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, title: str, quantity: int) -> None:

        if self.get_free_space() < quantity:
            raise NotEnoughSpace

        if title in self.__items:
            self.__items[title] += quantity

        else:
            self.__items[title] = quantity

    def remove(self, title: str, quantity: int) -> None:
        if title not in self.__items or self.__items[title] < quantity:
            raise NotEnoughProduct

        self.__items[title] -= quantity
        if self.__items[title] == 0:
            self.__items.pop(title)

    def get_free_space(self) -> int:
        current_space = 0
        for value in self.__items.values():
            current_space += value

        return self.__capacity - current_space

    def get_items(self) -> dict[str, int]:
        return self.__items



    def get_unique_items_count(self):
        return len(self.__items)
