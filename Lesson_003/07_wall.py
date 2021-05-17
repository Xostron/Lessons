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
lp = sd.get_point(rd.randint(-100,0), 0)
rp = sd.get_point(lp.x+length, lp.y+width)
sd.rectangle(lp, rp)
for _ in range(30):
    for _ in range(50):
        sd.rectangle(lp, rp)
        lp.x += length + step
        rp.x = lp.x + length
    lp.x = rd.randint(-100, 0)
    rp.x = lp.x + length
    lp.y = rp.y + step
    rp.y = lp.y + width + step

sd.pause()
