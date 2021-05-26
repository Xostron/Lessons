from random import randrange as rnd, choice, randint
import tkinter as tk
import math
import time




# ======================Init===================================================
tk1 = tk.Tk()  # объект рабочее окно
tk1.title("xostron")  # у рабочего окна есть имя
tk1.resizable(0, 0)  # рабочее окно - свойство неизменяемости окна
tk1.wm_attributes("-topmost", 1)  # рабочее окно - свойство рабочего окна поверх всех окон

# объект холст для рисования
canv1 = tk.Canvas(tk1, width=700, height=700, bd=0, highlightthickness=0)

btn = tk.Button(tk1, text="Нажми!")
btn2 = tk.Button(master=tk1, cnf = {'text':'master'})

btn.config(command=lambda: print("Привет, Tkinter!"))
btn.pack(padx=120, pady=30)
btn2.pack(padx = 200,pady = 200)

canv1.pack()  # отрисовка объекта холста - canv1 - если параметры холста без изменений(то 1 раз)
tk1.update()  # обновление объекта Ткинтер - (обновление рабочего окна - экрана) для анимации



def func(event):
    print('ashfsjdfhalksfjalskf')




# ======================InitEnd===================================================
x = 0
y = 0
# ======================InfinityCycle==+++++======================================
while 1:

    canv1.bind_all('<Button-2>', func)



    tk1.update_idletasks()  # вставляют всегда, а нахера не понятно
    tk1.update()  # обновление объекта Ткинтер - (обновление рабочего окна - экрана) для анимации
    time.sleep(0.01)  # пауза 10мс
