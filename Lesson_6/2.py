"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof


class Pearson:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 50
        self.armor = 1.2


class Pearson_slots:
    __slots__ = ['name', 'health', 'damage', 'armor']

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 50
        self.armor = 1.2


mr = Pearson('имя')
mrs = Pearson_slots('имя')

print(mr.__dict__)

print(asizeof.asizeof(mr))
print(asizeof.asizeof(mrs))