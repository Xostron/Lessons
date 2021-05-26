# создание множества
a = set() # пустое множество
a = {1, 2, 3, 1, 2, 3, 4, 5}
print(a, type(a))
c = set('abracadabra')
print(c, type(c))
d = set([1, 2, 3, 4, 5, 1, 2, 3, 1, 1, 1, ])
print(d, type(d))
e = set(range(10))
print(e, type(e))

# добавление
f = {10, 20, 30}
f.add(11)
f.update([5, 6, 20, 30])  # == f. add(5)  f. add(6) f. add(20) f. add(30)
f.update(range(100, 105))
f.update({12, 13, 25, 35})
print(f, type(f))

# удаление
f.discard(35)
print(f, type(f))

f.remove(100)
print(f, type(f))

print(f.pop())
print(f.pop())
print(f.pop())
print(f.pop())
print(f.pop())
print(f)

# полная очистка множества
f.clear()
print(f)

# операции над множествами
a = {1, 2, 3, 4}
b = {10, 4, 1, 20, 25}
# пересечения между 2мя множествами - общие элементы
print(a & b)
print(a.intersection(b))
a.intersection_update(b)
print(a)
# проверка принадлежит ли значение данному множеству
print(1 in a)
print(100 not in b)
print(a)
# объединение
a = {1, 2, 3, 4}
b = {10, 11, 12, 13, 3}
print(a | b)
c = {0,5,20}
a = a.union(c)
print(a)
# возврат у никальных значений из одного множества
d = {1,4,5,6}
a = {1, 2, 3, 4}
print(a-d)
# возврат уникальных значений от обоих множеств
d = {1,4,5,6}
a = {1, 2, 3, 4}
print(a^d)
# сравнения
d = {1,4,5}
a = {1, 5, 4,6}
print(a==d)
print(a<d)
print(a>d)

#множества не индексируются
#поэтому можно пройтись только по его значениям
for i in d:
    print(i)

#пример
text = input()
a = set()
while text !='':
    word = text.split()
    a.update(word)
    text = input()
print(a)
print(len(a))