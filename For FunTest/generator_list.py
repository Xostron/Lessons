# a = [float(i) for i in input().split(',')]
# a = [float(i) for i in input().split(',') if условие]
# print(a)
a = 'hello world'
a = a.strip()
a = a.split()
print(a)

a = [i ** 2 for i in range(10)]
print(a)

a = [i for i in 'hello']
print(a)

import random

a = [random.randint(-10, 10) for i in range(10)]
print(a)

a = [elem for elem in a if elem % 2 == 0]
print(a)

# a = input().split()
# a = [int(i) for i in a]
# print(a)

n = 5
m = 4
a = [[0] * m for i in range(n)]
print(a)
for i in a:
    print(i)

a = [i * j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i * j >= 10]
print(a)

"""Выражения-генераторы - итератор, элементы которого можно итерироватьтолько один раз
Итератор - объект, который поддерживает функцию ext(). Помнит о том, какой элемент
будет браться следующим
итерируемый объект - объект, который предоставляет возможность обойти поочередно
свои элементы. Может быть преобразован к итератору

"""
s = [1,2,3] # итерируемый объект
d = iter(s) # итератор
print(next(d))
print(next(d))
print(next(d))

# выражения-генераторы
b = (i**2 for i in range(1,6))
print(b)

c = list(b) # первое обращение к генератору
print(sum(b)) # второе обращение к генратору - =0, т.к. элементы генератора можно обойти только один раз
print(c)

"""Функция генератор. Создание генератора при помощи yield Python
"""
def genf():
    for i in [43,65,32]:
        yield i

s = genf()
print(next(s))
print(next(s))

for i in genf():
    print(i)

"""функция map"""
#map(функция, итерируемый объект)

#s = list(map(int, input().split()))
#print(s)

#s = [int(i) for i in input().split()]
#print(s)

"""Функция zip python. Что делает функция zip в Python
"""
a = [1,2,3,40]
b = [10,11,12,13]
for i in range(4):
    print(a[i], b[i])

a = [1,2,3,40]
c = ['a','b','c','d']
rez = zip(a,b,c)
#print(list(rez))

col1, col2, col3 = zip(*rez)
print(col1,col2,col3)

c = ['b','d','c','a']
c.sort()
print(c, '+++')

a = 'Kratos'
print('hello %s' % a)

s = 'god of war ragnarok'
print(s.split(' '))
a = s.split(' ')


print('+'.join(a))

print("================================================")

x=0.12
try:
    print(1/0)
except ZeroDivisionError:
    print(1)
else:
    print(2)
finally:
    print(3)
print(x)


def Foo(n):
    def mul(x):
        return x/n
    return mul

a=Foo(5)
print(a)
b=Foo(5)
print(a(3))
print(a(b(2)))

def hi(x):
    print("hero")
    #return x*3


a = hi(1)
b = hi(2)
print(id(a), id(b), id(hi))


_name = 0

print('===========================================')
i = sum = 0
print(id(i), id(sum))
print(i, sum)
while i<=4:
    sum+=i
    i=i+1
print(sum, i)