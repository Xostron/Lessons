# -*- coding: utf-8 -*-
import math

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

class CountText:
    def __init__(self, file_txt):
        self.file_name = file_txt

    def collect(self):
        self.stat = {}
        self.res = 0
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                            self.res += 1
                        else:
                            self.stat[char] = 1
                            self.res += 1

    def arrange(self, mode = 1):
        # по алфавиту по возрастанию
        if mode == 1:
            self.statList = list(self.stat.items())
            self.statList.sort(key=lambda x: x[0], reverse=False)

        #  - по алфавиту по убыванию
        if mode == 2:
            self.statList.sort(key=lambda x: x[0], reverse=True)

        #  - по частоте по возрастанию
        if mode == 3:
            self.statList.sort(key=lambda x: x[1], reverse=False)

    def terminalOut(self):
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')

        for key, val in self.statList:
            x = (10 - len(str(val))) // 2
            m = len(str(val))
            y = int(math.ceil((10 - m - (10 - m) / 2)))
            string = '|    ' + key + '    |' + ' ' * x + str(val) + ' ' * y + '|'
            print(string)
        print('+---------+----------+')
        print(f'|  итого  | {self.res}  |')
        print('+---------+----------+')


state = CountText('python_snippets/voyna-i-mir.txt')
state.collect()
state.arrange()
state.terminalOut()