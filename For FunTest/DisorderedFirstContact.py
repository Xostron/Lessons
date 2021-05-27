import sys
import math

n = int(input())
message = input()
print('INIT: ', n, message, len(message))

s = y = len(message)
xk = 0
while y >= 0:
    xk += 1
    y = s - (1 + xk) * xk / 2
print(xk)
combi = ''
if n < 0:  # encode
    for i in range(1, xk + 1):
        if i % 2 > 0:  # нечетные
            combi = combi + message[:i]
            message = message[i:]
            print(f"{i} нечетные: combi = {combi}, message = {message}")
        else:  # четные
            combi = message[:i] + combi
            message = message[i:]
            print(f"{i} четные: combi = {combi}, message = {message}")

if n > 0:  # decode
    for i in range(xk, 0, -1):

        if i % 2 == 0:
            if int(s - (1 + i) * i / 2) < 0:
                j = int(s - (1 + (i - 1)) * (i - 1) / 2)
                i = j
            combi = message[:i] + combi
            message = message[i:]
            print(f"{i} нечетные: combi = {combi}, message = {message}")
        else:
            k = len(message)
            combi = message[k - i:] + combi
            message = message[:k - i]
            print(f"{i} четные: combi = {combi}, message = {message}")
print(combi)

"""
-1
abcdefghij

1
ghibcadef


5
hitoeplmu eneicldts aide tsxt
"""
