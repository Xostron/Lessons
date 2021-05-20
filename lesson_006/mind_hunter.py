# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.

from random import randint
_thinkNumber = []
_supposedNumber = []


def thinkNumber():
    global _thinkNumber
    numb = str(randint(1000, 9999))
    _thinkNumber = [int(i) for i in numb]
    return _thinkNumber


def compareNumber(enterData : str):
    _supposedNumber = []
    # проверка на корректность входных данных и преобразование до нужного формата
    enterList = [i for i in enterData]
    #print(enterList)
    j = 0
    for i in enterList:
        try:
            numb = int(i)
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            j += 1 if numb > 0 else j
            if numb > 0 and j <= len(_thinkNumber):
                _supposedNumber.append(numb)
    [_supposedNumber.append(0) for _ in range(len(_supposedNumber)+1, 5, 1)]

    mask = [0, 0, 0, 0]
    # количество коров
    for i in enumerate(_supposedNumber):
        k = -1
        for j in enumerate(_thinkNumber):
            k += 1
            if i == j:
                mask[k] = 1
            elif i[1] == j[1] and mask[k] == 0:
                mask[k] = -1
    cow = 0
    bull = 0
    for i in mask:
        bull += 1 if i == 1 else 0
        cow += 1 if i == -1 else 0
    result = {'bull':0, 'cow':0}
    result['bull'] = bull
    result['cow'] = cow

    return result







