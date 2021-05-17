# -*- coding: utf-8 -*-
import random as rnd

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

radius = 50


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def buble(point,step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


# Нарисовать три ряда по 10 пузырьков
# Нарисовать 10 пузырьков в ряд
#for y in range(100,301,100):
#    for x in range (100,1001,100):
#        point = sd.get_point(x, y)
#        buble(point, 5)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = rnd.randint(2,10)
    buble(point, step)

sd.pause()


