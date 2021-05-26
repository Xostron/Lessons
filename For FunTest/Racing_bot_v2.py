from random import randrange as rnd, choice, randint
import tkinter as tk
import math
import time


class Flag():
    def __init__(self, canvas, num):
        self.objNum = num
        self.canvas = canvas
        self.destination = [0, 0]
        self.text_flag = ''
        self.text_numb = str(self.objNum)
        self.id = self.canvas.create_oval(self.destination[0] - 20, self.destination[1] - 20,
                                          self.destination[0] + 20,
                                          self.destination[1] + 20, fill='grey')
        self.info = canvas.create_text(self.destination[0], self.destination[1], text=self.text_flag)
        self.info2 = canvas.create_text(self.destination[0], self.destination[1], text=self.text_numb)
        self.start()

    def start(self):
        # init start coordinate flag
        self.center = self.destination = [randint(0, 600) for self.i in range(2)]
        self.text_flag = f"{self.destination[:]}"
        # print text
        self.canvas.itemconfig(self.info, text=self.text_flag)
        # set&draw new positiong flag
        self.canvas.coords(
            self.id,
            self.destination[0] - 20,
            self.destination[1] - 20,
            self.destination[0] + 20,
            self.destination[1] + 20)
        # set&draw new positiong text1 (current coordinate)
        self.canvas.coords(
            self.info,
            self.destination[0] - 20,
            self.destination[1] - 20)
        # set&draw new positiong text2 (numeration)
        self.canvas.coords(
            self.info2,
            self.destination[0],
            self.destination[1])


class Car():
    def __init__(self, canvas, *goals):
        self.flags = list(goals)
        self.canvas = canvas
        self.curr_flag = 0
        self.next_flag = 1
        self.xn = 0
        self.yn = 0
        self.vx = 0
        self.vy = 0
        self.width = 20
        self.height = 40
        self.color = 'red'
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.id = canvas.create_line(self.xn, self.yn, self.xn + self.width, self.yn + self.height, width=7,
                                     fill=self.color)
        self.pos_car = []
        self.an = 0
        self.center_flag = []

    def get_coor_flag(self):
        pos_flag = []
        self.center_flag = []
        # get coordinates of flags
        for flag in self.flags:
            pos_flag.append(self.canvas.coords(flag.id))
            center_flag_x = (pos_flag[flag.objNum][2] - pos_flag[flag.objNum][0]) / 2 + pos_flag[flag.objNum][0]
            center_flag_y = (pos_flag[flag.objNum][3] - pos_flag[flag.objNum][1]) / 2 + pos_flag[flag.objNum][1]
            self.center_flag.append([center_flag_x, center_flag_y])
        # print("0) Position FLAGS = ",pos_flag)
        print("1) Center FLAGS = ", self.center_flag)

    def coor_of_car(self):
        # coordinate of car
        self.center_car_x = self.center_flag[self.curr_flag][0]
        self.center_car_y = self.center_flag[self.curr_flag][1]
        self.pos_car = [self.center_car_x, self.center_car_y]

    def calc_dist_flag_car(self):
        distance = []
        # calculate distance between flags and car
        x1 = 0
        y1 = 1
        for i in range(3):
            distance.append(math.sqrt((self.center_flag[i][x1] - self.center_car_x) ** 2 +
                                      (self.center_flag[i][y1] - self.center_car_y) ** 2))
            if distance[i] < 10:
                self.curr_flag = i
        print("2) dist between F&C = %s" % distance)

        # flags cursor
        self.next_flag = self.curr_flag + 1
        if self.curr_flag == 2:
            self.next_flag = 0
        print("3) curr = %s, next = %s" % (self.curr_flag, self.next_flag))

        # direction car
        if ((self.center_flag[self.next_flag][y1] - self.pos_car[1]) > 0 and (
                self.center_flag[self.next_flag][x1] - self.pos_car[0]) > 0) \
                or ((self.center_flag[self.next_flag][y1] - self.pos_car[1]) < 0 and (
                self.center_flag[self.next_flag][x1] - self.pos_car[0]) > 0):
            self.an = math.atan((self.center_flag[self.next_flag][y1] - self.pos_car[1]) / (
                    self.center_flag[self.next_flag][x1] - self.pos_car[0]))
        elif (self.center_flag[self.next_flag][x1] - self.pos_car[0]) < 0:
            self.an = math.atan((self.center_flag[self.next_flag][y1] - self.pos_car[1]) / (
                    self.center_flag[self.next_flag][x1] - self.pos_car[0])) + math.pi
        elif (self.center_flag[self.next_flag][x1] - self.pos_car[0]) == 0:
            self.an = 0

    def set_coords(self):
        #self.start_setting()
        self.get_coor_flag()
        self.coor_of_car()
        self.calc_dist_flag_car()

        self.canvas.coords(self.id,
                           self.center_flag[self.curr_flag][0],
                           self.center_flag[self.curr_flag][1],
                           self.center_flag[self.curr_flag][0] + 20 * math.cos(self.an),
                           self.center_flag[self.curr_flag][1] + 20 * math.sin(self.an))

        self.pos_car = self.canvas.coords(self.id)

        print(f"4) posX1 = {self.pos_car[0]}, posY1 = {self.pos_car[1]}"
              f"posX2 = {self.pos_car[2]}, posY2 = {self.pos_car[3]}, an = {self.an}")

    def move(self):
        self.vx = 0.5 * math.cos(self.an)
        self.vy = 0.5 * math.sin(self.an)
        # self.vx+=0.001
        # self.vy+=0.001
        self.canvas.move(self.id, self.vx, self.vy)

    def start(self, event):
        pass


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

flag1 = Flag(canv1, 0)
flag2 = Flag(canv1, 1)
flag3 = Flag(canv1, 2)
flags = [flag1, flag2, flag3]
globalStart = False
car = Car(canv1, flag1, flag2, flag3)
car.set_coords()


def action_flag(event):
    global globalStart
    for i_flag in flags:
        i_flag.start()
    globalStart = True


# ======================InitEnd===================================================
x = 0
y = 0
# ======================InfinityCycle==+++++======================================
while 1:

    canv1.bind_all('<Button-2>', action_flag)

    if globalStart:
        car.set_coords()
        globalStart = False
    car.move()

    tk1.update_idletasks()  # вставляют всегда, а нахера не понятно
    tk1.update()  # обновление объекта Ткинтер - (обновление рабочего окна - экрана) для анимации
    time.sleep(0.01)  # пауза 10мс
