from courier import Courier
from exceptions import BaseError
from request import Request
from shop import Shop
from store import Store
import json

store = Store(items={
    "печенька": 12,
    "собачка": 12,
    "ёлка": 12
})

shop = Shop(items={
    "печенька": 1,
    "собачка": 2,
    "ёлка": 3
})

storages = {
    "магазин": shop,
    "склад": store
}


def main():
    print('\nДобрый день\n')

    while True:


        for storage_title in storages:
            print(f"В {storage_title}e хранится: \n")
            a = storages[storage_title].get_items()
            for key, value in a.items():
                print(key, ":", value, "\n")










        user_input = input(
            'Ввидите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Ввидите "стоп" или "stop", если хотите закончить:\n'
        )
        if user_input in ('stop', 'стоп'):
            break


        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as e:
            print(e.message)
            continue


        courier = Courier(
            request=request,
            storages=storages
        )

        try:
            courier.move()
        except BaseError as e:
            print(e.message)


if __name__ == '__main__':
    main()
