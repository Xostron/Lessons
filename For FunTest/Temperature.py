"""Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0."""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
t = []
for i in input():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t.append(int(i))

if t != []:
    result = abs(t[0])
    for i in t:
        if abs(i) == abs(result):
            result = abs(i)
        if abs(i)<result:
            result = i
        if n == 1:
            result = t[0]
        if n == 2 and t[0] == t[1]:
            result = t[0]
else:
    result = 0
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)



#1 var
input()  # skip
ln = input() or '0'

temps = [int(s) for s in ln.split()]

temps.sort(key = lambda x: (abs(x),-x))

#print(temps, file=sys.stderr)

print(temps[0])

#2
input()
T=[int(s) for s in input().split()]
print(T and sorted(sorted(T,reverse=True),key=abs)[0] or 0)
#3
input()  # the number of temperatures to analyse
value = lambda a : abs(a) + 0.1*(a <0)
print( min((int(i) for i in input().split()), key = value, default = 0))
#4
n       = int(input())  # the number of temperatures to analyse
temps   = input()  # the n temperatures expressed as integers ranging from -273 to 5526
print(min(temps.split(' '), key = lambda x: abs(int(x) - .1)) if n else 0)