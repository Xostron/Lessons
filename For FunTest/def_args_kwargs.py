a, b, c = 12, 15, 20
print(a, b, c)
# *a - список
# b = 55
# c = False
*a, b, c = [10, True, 'hero', 20, 55, False]  # = любой упорядоченный объект (список, кортеж, строка)
print(a, b, c)

s = [4, 10]  # list
print(range(1, 5))
print(list(range(1, 5)))
print(list(range(*s)))  # *s - распаковывает для функции range от 4 до 9


def f(a, b, c):
    print(a, b, c)


f(1, 2, 3)
a = ["hi", True, [1, 2, 10]]

f(*a)  # *a - распаковывается на 4 объекта для функции f(a,b,c,d)


# функция с произвольным количеством неименованных входных параметров
# все переменные на входе упаковываются в кортеж
#
def func(*args):
    print(args)


func(1, 2, 3, 4, 5, 6, a)


# Функция с неопределенным количеством именованных элементов
# все  именованные переменные на входе упаковываются в словарь, где имя переменной а, b - key, значения - value
# неименованные - в кортеж
def fu(**kwargs):
    print(kwargs)


fu(a=1, b=2)


# функция с параметрами - по умолчанию
def pr(*args, sep='$', end='%'):
    print(args, sep, end)


pr(1, 2, 3, 4, 100)
pr(10, 20, 30, 40, sep='+++')

a = [1, 3, 5, 7, 9]
print(a)
print(*a)


def example(*flag):
    print("testing")
    a = list(flag)
    print(a, type(a))


example(1,2,3,4,5)