# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
startPoint = sd.get_point(50, 50)
endPoint = sd.get_point(350, 450)
step = 7
for color in rainbow_colors:
    sd.line(startPoint, endPoint, color, 4)
    startPoint.x += step
    endPoint.x += step
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
point = sd.get_point(350,-50)
radius = 600
for color in rainbow_colors:
    sd.circle(point,radius, color, 40)
    radius -=20
sd.pause()
