"""
4
5
E
 #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###
# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #
### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##
# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #
# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #


https://www.codingame.com/ide/puzzle/ascii-art

TOP 1

l = int(input())
h = int(input())
t = input()
row = [input() for i in range(h)]

for j in range(h):
    for i in t:
        asc=(ord(i.upper())-65) if i.isalpha() else 26
        print(row[j][(l*asc):(l*(asc+1))],end='')
    print()

TOP 2
l = int(input())
h = int(input())
t = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
for i in range(h):
    row = input()
    s = ""
    for c in t.upper():
        if c not in alphabet:
            c = '?'
        i = alphabet.index(c)
        s += row[i*(l):(i+1)*(l)]
    print(s)

"""
# TODO function to convert input data (A..Z?) to dictionary {"A": ([x,x,x,x],[x,x,x,x],[x,x,x,x],[x,x,x,x],[x,x,x,x])}
# [x,x,x,x] - element in row = width_symbol
# [x,x,x,x],[x,x,x,x],[x,x,x,x],[x,x,x,x],[x,x,x,x] - number of rows =  height_symbol
# 65 - 90 = A..Z
# 97 - 122 = a..z


def rawToDict(width_symbol, height_symbol, dataList):
    """
    function to convert input data (A..Z?) to dictionary
    {"A": [[x,x,x,x],[x,x,x,x],[x,x,x,x],[x,x,x,x],[x,x,x,x]], ... "Z":}
    :param width_symbol:
    :param height_symbol:
    :param dataList:
    :return:
    """
    j = height_symbol
    key = 64
    dictionary = {}
    for i in range(0, len(dataList[0]), width_symbol):
        key += 1
        shortList = []
        for x in range(len(dataList)):
            shortList.append(dataList[x][i:i+width_symbol])
            if key > 90:
                key = 63
            dictionary[f'{chr(key)}'] = shortList
    return dictionary

def printDict(string): # печать по одному символу с новой строки
    dataStr = string.upper()
    for symbol in dataStr:
        if 90>=ord(symbol) >= 65:
            for i in dictionary[symbol]:
                print(''.join(i))
        else:
            for i in dictionary['?']:
                print(''.join(i))

def printString(string, height_symbol, dict):
    dictionary = dict.copy()
    inputStr = string.upper()
    stringOfdict = []
    j = 0
    while j != height_symbol:
        for symbol in inputStr:
            if symbol in dictionary.keys():
                stringOfdict.append(dictionary[symbol][j])
            else:
                stringOfdict.append(dictionary["?"][j])
        j += 1
    step = len(inputStr)
    start = 0
    end = step
    a = []
    b = ''
    for i in range(height_symbol):
        for j in stringOfdict[start:end]:
            a = j
            b = b + ''.join(a)
        print(b)
        start = end
        end = start+step
        b = ''


dictionary = {}
width_symbol = int(input())
height_symbol = hs_i = int(input())
symbols = input()
graphicsList = []

while hs_i > 0:
    graphicsList.append([i for i in input()])
    hs_i -= 1


dictionary = rawToDict(width_symbol, height_symbol, graphicsList)
printString(symbols, height_symbol = height_symbol, dict = dictionary)





