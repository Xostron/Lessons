import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

mountain_h = []
# pre = []
# m = []
first = True

# game loop
while True:
    mountain_h = []
    for i in range(8):
        mountain_h.append(int(input()))  # represents the height of one mountain.

    if first:
        pre = mountain_h.copy()
        m = mountain_h.copy()
        first = False

    if pre != mountain_h:
        for i in range(8):
            if pre[i] != mountain_h[i] and mountain_h[i] > 0:
                m[i] = mountain_h[i]
        pre = mountain_h.copy()

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    val_max = max(m)
    i_max = m.index(val_max)
    m[i_max] = 0
    # The index of the mountain to fire on.
    print(str(i_max))


"""Analog
#1 var
while True:
    print(max([(int(input()),x) for x in range(8)])[1])
    
#2Var
while True:
    print(max(range(8), key=lambda _: input()))
    
#3Var
while True:
    mountains = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0.
        mountains.append(mountain_h)
    print(mountains.index(max(mountains)))
    
#4Var
while True:
    highest = -1
    index_highest = -1    
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0.
        if ( mountain_h > highest ) :
            highest = mountain_h
            index_highest = i          

    # The number of the mountain to fire on.
    print(index_highest)
"""