import  simple_draw as sd
import random

def drawSnow(startPoint, length = 10, n = 10, color = sd.COLOR_DARK_CYAN):
    """
    Рисование снежинки
    :param startPoint:
    :param length: длина луч
    :param n: количество лучей
    :return:
    """
    step = 360 / n
    angle_i = 0
    sd.circle(startPoint,color = color, width = 2, radius=10)
    #for i in range(n):
        #vektor = sd.get_vector(startPoint, angle_i, length = 10)
        #angle_i += step
        #sd.line(vektor.start_point, vektor.end_point, color = color, width=2)


def plentySnow():
    """
    i - кол-во снежинок по оси Х
    j - кол-во снежинок по оси У
    :return: список снежинок list snow
    """
    snows = []
    snows = [sd.get_point(i, j) for i in range(50, 500, 40) for j in range(500, 400, -40)]
    return snows



def moveSnow(snowPoint, speedX, speedY, length = random.randint(5, 20)):
    """
    Сдвиг снежинки: 1 шаг - закрасить снежинку фоном
    2 шаг - отрисовать новую со смещением по х, у
    :param snowPoint:
    :param speedX:
    :param speedY:
    :param length:
    :return:
    """
    drawSnow(snowPoint, color = sd.background_color)
    snowPoint.x += speedX
    snowPoint.y += speedY
    drawSnow(snowPoint, color = sd.COLOR_DARK_CYAN, length = length)
    return snowPoint




def falldown(snowPoint, downBorder = 300):
    """
    Возвращает True - когда снежинка достигла downBorder
    :param snowPoint:
    :param downBorder:
    :return:
    """
    if snowPoint.y <= downBorder:
        return True
    return False



def deleteSnow(snowPoint):
    """
    закрасить снежинку фоном (удаление)
    :param snowPoint:
    :return:
    """
    drawSnow(snowPoint, color = sd.COLOR_BLUE)




