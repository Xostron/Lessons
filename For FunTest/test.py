goods = ['banana', 'orange', 'apple', 'banana', 'orange', 'banana', 'apple', 'apple', 'apple']
from operator import itemgetter
def foo(list):
    res = []
    ref = set(list)
    for item in ref:
        n = 0
        for q in list:
            if item == q:
                n += 1
        res.append((item, n))
    res.sort(key = itemgetter(1), reverse = True)
    print(res)


foo(goods)

