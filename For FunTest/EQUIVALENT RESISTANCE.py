"""

https://www.codingame.com/ide/puzzle/equivalent-resistance-circuit-building

=============================================
2
A 20
B 10
( A B )

Output
30.0
=============================================
2
C 20
D 25
[ C D ]

Output
11.1
=============================================
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
def detFormula(formula):
    separate = ['[', '(', ']', ')']
    openSqr = 0
    openCrl = 0
    indexIn = -1
    indexOut = -1
    lastSymbol = ''
    computeList = []
    equ = 0
    print(list(enumerate(formula)))
    for symbol in enumerate(formula):

        if openSqr > 0 and indexIn != -1:
            if symbol[1] == '[':
                print(f"1find openSqr {openSqr}")
                openSqr += 1
            if symbol[1] == ']':
                print(f"2find openSqr {openSqr}")
                openSqr -= 1
            if openSqr == 0:
                indexOut = symbol[0]
                lastSymbol = ']'
                print(f"find indexOut Sqr {indexOut}")
        if openCrl > 0 and indexIn != -1:
            if symbol[1] == '(':
                openCrl += 1
                print("1find openCrl")
            if symbol[1] == ')':
                openCrl -= 1
                print('2find openCrl')
            if openCrl == 0:
                indexOut = symbol[0]
                lastSymbol = ')'
                print('3find indexOut Crl')
        if openSqr == 0 and openCrl == 0 and indexIn == -1:
            if symbol[1] == '[':
                print(f"3find openSqr {openSqr}")
                openSqr += 1
                indexIn = symbol[0]
            if symbol[1] == '(':
                print(f"4find openCrl {openCrl}")
                openCrl += 1
                indexIn = symbol[0]



        if indexIn != -1 and indexOut != -1:
            print('%%%%%%%%%%%%%%%%%%%')
            computeList = formula[indexIn + 1:indexOut]
            if len(computeList) == 2:
                if lastSymbol == ']':
                    equ = 0
                    for i in computeList:
                        equ += 1 / (dictionary[i])
                        print(f"*****{dictionary[i]}")
                    equ = 1 / equ
                elif lastSymbol == ')':
                    equ = 0
                    for i in computeList:
                        equ += dictionary[i]
                        print(f"*****{dictionary[i]}")
                print(f"OUT: {computeList} "
                  f"Result = {equ} "
                  f"LastSymbol = {lastSymbol} ")
    return [indexIn, indexOut, equ]


n = int(input())
inputs = [input().split() for _ in range(n)]
for i in range(n):
    inputs[i][1] = int(inputs[i][1])
circuit = input()
formula = [i for i in circuit if i != ' ']
dictionary = dict(inputs)
result = 0
res = []
while result == 0:
    res = detFormula(formula)
    print(f'I am the result: {res}')
    for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if not s in dictionary:
            dictionary[s] = res[2]
    formula = formula[res[0]+1: res[1]]
    if len(formula) <= 2:
        out = res[2]
        result = 1
    print(f"===== {formula}")






# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("Equivalent Resistance")