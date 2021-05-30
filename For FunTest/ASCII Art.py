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

def rawToDict(width_symbol, height_symbol, inputData):
    pass

width_symbol = int(input())
height_symbol = int(input())
symbol = input()
graphicsList = []




while height_symbol>0:
    graphicsList.append([i for i in input()])
    height_symbol -= 1



print(len(graphicsList))
print(graphicsList)
