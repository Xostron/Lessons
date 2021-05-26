import sys
import math
def search(data):
    flag1 = True
    data1 = []
    while flag1:
        _min = min(data)
        _i_min = data.index(_min)
        if _i_min == 0:
            data = data[1:]
            flag1 = True
        else:
            data1 = data[:_i_min]  # begin...find min
            data2 = data[_i_min+1:]
            flag1 = False
        if len(data) == 1:
            return [0, [0]]
    _max = max(data1)
    delta1 = _min - _max
    return [delta1, data2]
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
v = []
data = []
n = int(input())
for i in input().split(' '):
    data.append(int(i))
print(n, data)


res = search(data)
delta1 = res[0]
data2 = res[1]
print(res)


delta2 = 0
if len(data2) > 1:
    res2 = search(data2)
    delta2 = res2[0]

print(delta1) if delta1<delta2 else print(delta2)








"""

delta = 0
k = 0
for i in v[0:n-2]:
    k += 1
    for j in v[k:]:
        if i-j > delta:
            delta = i-j
"""

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("answer")




"""
6
3 2 10 7 15 14
"""