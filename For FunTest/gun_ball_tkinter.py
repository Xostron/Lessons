from random import randrange as rnd, choice
import tkinter as tk
import math
import time


class ball():
    def __init__(self, canvas, xn, yn):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.canvas = canvas
        self.xn = xn
        self.yn = yn
        self.x = 0
        self.y = 0
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canvas.create_oval(
            self.xn - self.r,
            self.yn - self.r,
            self.xn + self.r,
            self.yn + self.r,
            fill=self.color
        )
        self.canvas.itemconfig(self.id, state="hidden")
        self.live = 30
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.ax = 0
        self.ay = 0.2
        self.vy_max = 0
        self.vx_max = 0
        self.start = 0
        self.flag1 = 0

    def set_coords(self, x, y):
        self.canvas.coords(
            self.id,
            x - self.r,
            y - self.r,
            x + self.r,
            y + self.r)
        self.x = 0
        self.y = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        #pos_ball[0,1,2,3] = x1,y1,x2,y2
        pos_ball = self.canvas.coords(self.id)
        if pos_ball[1] <= 0:
            self.vy = self.vy * - 1
        if pos_ball[0] <= 0:
            self.vx = self.vx * - 1
        if pos_ball[2] >= self.canvas_width:
            self.vx = self.vx * - 1



        if self.start == 1: # flag of starting ball
            self.vy += self.ay  #замедление по осиУ с каждой итерацией
            if self.ay < 0.5:   #начальное значение ау = 0.2
                self.ay += 0.05 #с каждой итерацией увеличиваем на 0.05, регулирование силы тяжести, большое значение будет быстрее уменьшать начальную скорость vy, мячик сразу будет падать
            if pos_ball[3] >= self.canvas_height: # проверка нижней границы
                if self.flag1 == 0: #первое касание с границей
                    self.vy = abs(self.vy_max/1) * -1 # при касании
                    self.flag1 = 1
                else: # последующие касания с угасанием
                    self.vy = abs(self.vy_max / 1.5) * -1
                self.vy_max = self.vy # фиксация скорости
                self.ay = 0.1
            if abs(self.vy_max) <= 0.5: # когда скорость загасится до минимального уровня, постепенно останавливаем движение мяча по осиХ
                if self.vx > 0:
                    self.vx -= 0.2
                if self.vx < 0.1:   # полный останов
                    self.vx = 0
                    self.vy = 0
        self.x = self.vx #скорость = шаг перемещения по пикселям
        self.y = self.vy
        self.canvas.move(self.id, self.x, self.y) # встроенная функция перемещения


class Gun():  # create object
    def __init__(self, canvas, color_calm, color_power):
        self.canvas = canvas
        self.color_calm = color_calm
        self.color_power = color_power
        self.id = canvas.create_line(20, 450, 40, 420, width=7)  # FIXME: don't know how to set it...
        self.f2_power = 20
        self.f2_on = 0
        self.an = 1
        self.inc_power = False
        self.numb_ball = -1
        self.ball_vx = 0
        self.ball_vy = 0
        self.xk = 20 + self.f2_power * math.cos(self.an)
        self.yk = 450 + self.f2_power * math.sin(self.an)
        self.id_score = canvas.create_text(150, 100, text="счет: " + str(self.f2_power) +
                                                          '\n xk = ' + str(self.xk) +
                                                          '\n yk = ' + str(self.yk) +
                                           '\n numb_ball =' + str(self.numb_ball) +
                                           '\nVx = ' + str(self.ball_vx) +
                                           '\nVy = ' + str(self.ball_vy),
                                           font="Verdana 12")
        self.arr_ball = []

    def fire2_start(self, event):
        self.f2_on = 1
        self.numb_ball += 1
        self.arr_ball += [ball(self.canvas, self.xk, self.yk)]
        self.arr_ball[self.numb_ball].vx = 0
        self.arr_ball[self.numb_ball].vy = 0
        """ ограничитель кол-ва мячиков
        if self.numb_ball >= 10:
            for i in range(len(self.arr_ball)):
                self.canvas.itemconfig(self.arr_ball[i].id, state = 'hidden')
            self.arr_ball = []
            self.numb_ball = 0
            self.arr_ball += [ball(self.canvas, self.xk, self.yk)]

    """

    def fire2_end(self, event):
        self.anv = math.atan((event.y - self.arr_ball[self.numb_ball].yn) / (event.x - self.arr_ball[self.numb_ball].xn))
        self.ball_vx = self.arr_ball[self.numb_ball].vx_max = self.arr_ball[self.numb_ball].vx = self.f2_power/4 * math.cos(self.anv)
        self.ball_vy = self.arr_ball[self.numb_ball].vy_max = self.arr_ball[self.numb_ball].vy = self.f2_power/4 * math.sin(self.anv)
        self.arr_ball[self.numb_ball].set_coords(self.xk, self.yk)
        self.canvas.itemconfig(self.arr_ball[self.numb_ball].id, state="normal")
        self.arr_ball[self.numb_ball].start = 1
        self.f2_on = 0

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            self.canvas.itemconfig(self.id, fill=self.color_power)
        else:
            self.canvas.itemconfig(self.id, fill=self.color_calm)

    def power_up(self):
        # характер изменения длины линии
        if self.f2_on:
            if not self.inc_power and self.f2_power < 100:
                self.f2_power += 1
            else:
                self.inc_power = True
            if self.inc_power and self.f2_power > 21:
                self.f2_power -= 1
            else:
                self.inc_power = False
            self.canvas.itemconfig(self.id, fill=self.color_power)
        else:
            self.canvas.itemconfig(self.id, fill=self.color_calm)
            self.inc_power = False
        # отрисовка изменение длины линии

        self.canvas.coords(self.id, 20, 450,
                           20 + self.f2_power * math.cos(self.an),
                           450 + self.f2_power * math.sin(self.an))
        self.canvas.itemconfig(self.id_score, text="счет: " + str(self.f2_power) +
                                                   '\nxk = ' + str(self.xk) +
                                                   '\nyk = ' + str(self.yk) +
                                                    '\n ball = ' + str(self.numb_ball) +
                                                    '\nVx = ' + str(self.ball_vx) +
                                                    '\nVy = ' + str(self.ball_vy))
        # данные для мячика
        # 1 - coordinates
        self.xk = 20 + self.f2_power * math.cos(self.an)
        self.yk = 450 + self.f2_power * math.sin(self.an)

    def collision(self):
        if self.numb_ball>2:
            for i in range(0, len(self.arr_ball)-1):
                for j in range(i+1, len(self.arr_ball)):
                    pos_ball1 = self.canvas.coords(self.arr_ball[i].id)
                    center_ball_x1 = (pos_ball1[2] - pos_ball1[0])/2 + pos_ball1[0]
                    center_ball_y1 = (pos_ball1[3] - pos_ball1[1])/2 + pos_ball1[1]

                    pos_ball2 = self.canvas.coords(self.arr_ball[j].id)
                    center_ball_x2 = (pos_ball2[2] - pos_ball2[0]) / 2 + pos_ball2[0]
                    center_ball_y2 = (pos_ball2[3] - pos_ball2[1]) / 2 + pos_ball2[1]

                    distance = math.sqrt((center_ball_x2 - center_ball_x1)**2 +
                                         (center_ball_y2 - center_ball_y1)**2)
                    if distance < 20:
                        self.arr_ball[i].vx *= -1
                        self.arr_ball[i].vy *= -1
                        self.arr_ball[j].vx *= -1
                        self.arr_ball[j].vy *= -1

# ======================Init===================================================
tk1 = tk.Tk()  # объект рабочее окно
tk1.title("xostron")  # у рабочего окна есть имя
tk1.resizable(0, 0)  # рабочее окно - свойство неизменяемости окна
tk1.wm_attributes("-topmost", 1)  # рабочее окно - свойство рабочего окна поверх всех окон

# объект холст для рисования
canv1 = tk.Canvas(tk1, width=700, height=700, bd=0, highlightthickness=0)
#
canv1.pack()  # отрисовка объекта холста - canv1 - если параметры холста без изменений(то 1 раз)
tk1.update()  # обновление объекта Ткинтер - (обновление рабочего окна - экрана) для анимации

gun1 = Gun(canv1, "gray", "red")  # пользовательский объект - Пушка


# ======================InitEnd===================================================

# ======================InfinityCycle==+++++======================================
while 1:
    canv1.bind('<Motion>', gun1.targetting)  # отслеживание движения мыши и вызов метода объекта gun1
    canv1.bind('<Button-1>', gun1.fire2_start)
    canv1.bind('<ButtonRelease-1>', gun1.fire2_end)
    gun1.power_up()
    for i in range(0, len(gun1.arr_ball)):
        gun1.arr_ball[i].move()
    gun1.collision()
    #gun1.new_ball.move()
    tk1.update_idletasks() # вставляют всегда, а нахера не понятно
    tk1.update()  # обновление объекта Ткинтер - (обновление рабочего окна - экрана) для анимации
    time.sleep(0.01)  # пауза 10мс
