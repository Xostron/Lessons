# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
class NOK:
    def __init__(self, inFile, outFile ):
        self.inFile = inFile
        self.outFile = outFile
        pass

    def collect(self):
        self.collection = []
        self.all = 0
        with open(self.inFile, 'r') as file:
            for line in file:
                self.all += 1
                if 'NOK' in line:
                    self.collection.append(line)
        #print(self.collection)

    def out(self):
        self.count = 0
        with open(self.outFile, 'w') as file:
            for line in self.collection:
                file.write(line)
                self.count += 1
            file.write(f'Result {self.count} NOK from all values = {self.all}')

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


inPath = 'events.txt'
outPath = 'outData.txt'

nok = NOK(inPath, outPath)
nok.collect()
nok.out()