# dict - словарь (ассоциативный массив)
# create dictionary
from operator import itemgetter
# 1st way
d = {
    # key:value
    'moskva':495,
    'piter': 812,
    'penza': 8412
}
print(d)

# 2nd way
r = dict(moskva=495, piter = 812, penza = 8412)
print(r)

# 3rd way
a = [['st', 1],["nd", 2],['rd', 3]]
t = dict(a)
print(t)

# 4th way
q = dict.fromkeys(['a','b','c'], 100)
print(q)

# 5th way
v = dict()
print(v)

#Взаимодействие со словарем

print(d['penza'])

# delete element
del t['st']
print(t)

print('rd' in t) # проверка ключа на наличие в словаре
print(len(t))

if 'xxx' in t:
    print(t['xxx'])
else:
    t['xxx'] = 104
print(t)

for key in d:
    print(key, d[key])

# Methods
# full clear dictionary
d.clear()
print(d)

# return value - возвращает по ключу значение, если ключа нет, то возвращает то что во 2 параметре
print(t.get('s', 'no such key'))

# возвращает по ключу значение, если ключа нет, то создает запрашиваемый ключ со значением из 2го параметра
print(t.setdefault('xxx', 111))
print(t)

#Удаление элемента только по ключу
print(t.pop('rd'))
print(t)

#Удаление элемента - случайный элемент
a = {
    1: "a",
    2: "b",
    3: "c",
    4: "d"}
print(a)
print(a.popitem())
print(a)


b = a.keys()
print(b, type(b)) # return объект dict_keys только ключи

b = a.values()
print(b, type(b)) # return объект dict_values только значения

b = a.items()
print(b, type(b)) # return объект dict_items ключ+значение = кортежи

