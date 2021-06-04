"""
3
A 24
B 8
C 48
[ ( A B ) [ C A ] ]

Output
10.7
=============================================
"""


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
# for i in range(n):
#     inputs = input().split()
#     name = inputs[0]
#     r = int(inputs[1])
inputs = [input().split() for _ in range(n)]
for i in range(n):
    inputs[i][1] = int(inputs[i][1])
circuit = input()
formula = [i for i in circuit if i != ' ']
inputss = dict(inputs)

# for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     if not s in inputss.keys():
#         inputss[s] = 1
#
# inputss['X'] = 100
# print(f'количество {n}')
# print(f'формула {formula}')
# print(f"переменная {inputs[0][0]} = {inputs[0][1]}")
# print(f"переменная {inputs[1][0]} = {inputs[1][1]}")
# print(f"переменная {inputs[2][0]} = {inputs[2][1]}")
# print(inputss)
for symbol in enumerate(formula):
    print(symbol, symbol[0], symbol[1])