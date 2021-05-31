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
    j = height_symbol
    key = 64
    dictionary = {}

    print('================================')

    for i in range(0, len(dataList[0])-width_symbol, width_symbol):
        key += 1
        shortList = []
        for x in range(len(dataList)):
            shortList.append(dataList[x][i:i+width_symbol])
            dictionary[f'{chr(key)}'] = shortList
            print(shortList)
    return dictionary


dictionary = {}
width_symbol = int(input())
height_symbol = hs = int(input())
symbol = input()
graphicsList = []

while height_symbol > 0:
    graphicsList.append([i for i in input()])
    height_symbol -= 1





dictionary = rawToDict(width_symbol, hs, graphicsList)

#dictionary['A'] = [1,2,3]

print(dictionary)


