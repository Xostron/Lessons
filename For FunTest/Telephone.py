


goal = 0
telephone = []
i=0
while i<5:
    i+=1
    telephone.append(input())
#telephone = list(iter(input, ''))
#print(telephone)
"""
telephone = [i for i in input().split(' ')]

"""
maxLenNumb = len(telephone[0])
refNumb = telephone[0]
for max in telephone:
    if len(max) > maxLenNumb:
        maxLenNumb = len(max)
        refNumb = max
#print(refNumb, maxLenNumb)


for i in range(maxLenNumb): # срез опорной строки с номером телефона
    goal += 1
    save = []
    for numb in telephone:
        targetNumb = numb
        if i < len(targetNumb):
            if refNumb[0:i + 1:] != targetNumb[0:i + 1:] and not(targetNumb[0:i + 1:] in save):
                goal += 1
                save.append(targetNumb[0:i+1])
                #print(f"{goal}: {refNumb[0:i + 1:]} != {targetNumb[0:i + 1:]}"
                      #f"    Состояние: {save}")


print(goal)

"""
0412578440
0412199803
0468892011
112
15
"""


