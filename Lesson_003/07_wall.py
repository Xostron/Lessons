# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
import random as rd
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
length = 40
width = 20
step = 5
# TODO здесь ваш код
leftPoint = sd.get_point(-20, 5)
rightPoint = sd.get_point(leftPoint.x+length, leftPoint.y+width)
sd.rectangle(leftPoint, rightPoint)
row=-1
for _ in range(0, sd.resolution[1], width):
    row+=1
    for _ in range(0, sd.resolution[0], length):
        sd.rectangle(leftPoint, rightPoint)
        leftPoint.x += length + step
        rightPoint.x = leftPoint.x + length
    if row%2 == 0:
        leftPoint.x = 0
    else:
        leftPoint.x = -20
    rightPoint.x = leftPoint.x + length
    leftPoint.y = rightPoint.y + step
    rightPoint.y = leftPoint.y + width + step

sd.pause()
