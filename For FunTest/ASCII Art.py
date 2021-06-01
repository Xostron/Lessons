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

def printString(string, hs):
    dataStr = string.upper()
    string_dict = []
    j = 0
    while j != hs:
        for symbol in dataStr:
            if symbol in dictionary.keys():
                string_dict.append(dictionary[symbol][j])
        j += 1
    #print(string_dict, len(string_dict), len(string_dict[0]))


    step = len(dataStr)
    start = 0
    end = step
    a = []
    b = ''
    # #print(string_dict[start:end])
    for i in range(hs):
        for j in string_dict[start:end]:
            a = j
            b = b + ''.join(a)

        print(b)
        #print(string_dict[start:end])
        start = end
        end = start+step
        a = []
        b = ''
    #for i in range(hs):
    #print(string_dict[start:end], len(string_dict[start:end]))
    #print(''.join(string_dict[start:end]))


dictionary = {}
width_symbol = int(input())
height_symbol = hs = int(input())
symbol = input()
graphicsList = []

while height_symbol > 0:
    graphicsList.append([i for i in input()])
    height_symbol -= 1

print(graphicsList)
print(len(graphicsList[0]))
print(len(graphicsList[1]))
print(len(graphicsList[2]))
print(len(graphicsList[3]))
print(len(graphicsList[4]))

dictionary = rawToDict(width_symbol, hs, graphicsList)


printString('ZZ', 5)





