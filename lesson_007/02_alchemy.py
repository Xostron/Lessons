# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Element:
    elements = {
        "Вода + Воздух": 'Шторм',
        "Вода + Огонь": 'Пар',
        "Вода + Земля": 'Грязь',
        "Воздух + Огонь": 'Молния',
        "Воздух + Земля": 'Пыль',
        "Огонь + Земля": 'Лава',
        "Свет + Воздух": 'Волна',
        "Свет + Огонь": 'Радиация',
        "Свет + Земля": 'Плазма',
        "Свет + Вода": 'Радуга'
    }

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        self.s = f"{str(self.part1)} + {str(self.part2)}"
        try:
            return Element.elements[self.s]
        except KeyError:
            return "None"


class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        return Element(part1=self, part2=other)


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        return Element(part1=self, part2=other)


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        return Element(part1=self, part2=other)


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        return Element(part1=self, part2=other)

class Light:
    def __str__(self):
        return 'Свет'

    def __add__(self, other):
        return Element(part1=self, part2=other)

a = Air()
b = Fire()
c = a + b
print(c)
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
