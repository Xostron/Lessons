# общие
import os
import time
import datetime
# kivy
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivymd.color_definitions import colors
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton, MDFloatingActionButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.icon_definitions import md_icons
from kivymd.uix.selection import MDSelectionList
from kivymd.uix.list import TwoLineAvatarListItem, MDList
from kivy.uix.scrollview import ScrollView
# database local
import sqlite3






Window.size = (350, 600)

with open(file="callelement.kv", encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class Note(MDFloatLayout):
    """иконки заметок"""

    def __init__(self, **kwargs):
        self.click = False
        self.selected = False
        self.help_selected = False
        self.flag_reaction = False
        super(Note, self).__init__(**kwargs)

    def Helper_CSF(self, instance):
        a.time_1st = time.time()
        self.help_selected = True
        print(f"нажата заметка - Helper {a.time_1st}")
        for i in ListNotes:
            if i.help_selected:
                i.help_selected = False
                self.obj = i
                break
        # print(dir(obj)) # позволяет увидеть все поля объекта
        if not a.flag_selected:
            self.anim = Animation(
                my_angle=360,
                d=self.obj.my_delay,
                t="in_sine", )
            self.anim.start(self.obj)
            self.my_color_circle_outer = (.3, .5, .8, 1)

    def Create_select_func(self, instance):
        a.time_2nd = time.time()
        time_res = round(a.time_2nd - a.time_1st, 2)
        print(f"Нажата заметка - Create_Select_func {time_res}")
        if not a.flag_selected:
            # если нет выделенных заметок
            if time_res >= self.my_delay:
                a.flag_selected = True  # есть выделенные заметки
            else:
                # не выделяем текущую заметку
                self.my_color_circle_outer = (.7, .7, .7, 1)
                self.anim.cancel_all(self.obj, 'my_angle')
                self.my_angle = 0
            if time_res >= self.my_reaction and time_res <= self.my_delay:
                self.flag_reaction = True
        if not a.flag_selected:
            if not self.flag_reaction:
                # если нет выделенных заметок
                print(f"Click on note - ++++++{a.flag_selected}", instance)
                screen_edit_note.ids.Input_Title.text = self.full_title
                screen_edit_note.ids.Input_Body.text = self.full_text
                sm.switch_to(ScreensList[1])
                self.click = True
            else:
                self.flag_reaction = False
        elif not self.selected:
            # если есть выделенные заметки и текущая заметка не выделена
            self.selected = True
            a.count_selection += 1
            a.item_selection.append(self.my_id)
            self.my_color_circle_outer = (.3, .5, .8, 1)
            self.my_angle = 0
            self.md_bg_color = (.3, .5, .8, 1)
            print(f"Количество выбранных = {a.count_selection}")
        else:
            self.selected = False
            self.md_bg_color = (.7, .7, .7, 1)
            a.count_selection -= 1
            a.item_selection.remove(self.my_id)
            for i in ListNotes:
                if i.selected:
                    a.flag_selected = True
                    break
                else:
                    a.flag_selected = False

        if a.flag_selected:
            main_tool.ids.tool_bar.left_action_items = [["close", lambda x: Unselected_all(), ]]
            main_tool.ids.tool_bar.right_action_items = [["trash-can", lambda x: Delete_selected(), ],
                                                         ["dots-vertical"]]
            main_tool.ids.tool_bar.title = f"{a.count_selection}"
        else:
            main_tool.ids.tool_bar.left_action_items = [['']]
            main_tool.ids.tool_bar.right_action_items = [['']]
            main_tool.ids.tool_bar.title = "Notes"


class CallNotes(MDGridLayout):
    """слой для иконок"""
    pass


class Tool(MDScreen):
    """верхняя строка меню - главный экран"""
    pass


class CustomBtn(MDFloatingActionButton):
    """кнопка - создать заметку"""

    def __init__(self, **kwargs):
        self.click = False
        super(CustomBtn, self).__init__(**kwargs)

    def add_note(self, instance):
        """метод - создание заметки"""
        global ScreensList, screen_edit_note
        # добавление заметки на слой
        ListNotes.append(Note())
        sm.switch_to(ScreensList[1])
        print(f"Created {len(ListNotes)}++++{a.flag_selected}")
        screen_edit_note.ids.Input_Title.text = ""
        screen_edit_note.ids.Input_Body.text = ""
        self.click = True
        for i in ListNotes:
            i.selected = False
            i.md_bg_color = (.7, .7, .7, 1)
        a.flag_selected = False
        a.count_selection = 0


def ParseShortName(ori, length):
    """
    Функция копирования строки ori в строку res имеющей фиксированную длину length
    c фильтром для символа "переход каретки"
    """
    res = ''
    for i in ori[:length]:
        if i != '\n':
            res += i
        else:
            break
    res += "..."
    return res


def Unselected_all():
    """
    """
    for i in ListNotes:
        i.selected = False
        i.md_bg_color = (.7, .7, .7, 1)
    a.flag_selected = False
    a.count_selection = 0
    main_tool.ids.tool_bar.left_action_items = [['']]
    main_tool.ids.tool_bar.right_action_items = [['']]
    main_tool.ids.tool_bar.title = "Notes"


def Delete_selected():
    """
    """
    print(f'{len(ListNotes)}***************1****************')
    for note in ListNotes[len(ListNotes)::-1]:
        if note.selected:
            print(f'delete - {note.selected}')
            MyLayout.remove_widget(note)
            ListNotes.remove(note)
    Unselected_all()
    #
    print('@@@@@ deleting list ', a.item_selection)
    #Delete_note_DB(connection=connection, cursor=cursor, note_id=a.item_selection[0])
    for i in a.item_selection:
        print('check deleting', i, type(i))
        Delete_note_DB(connection=connection, cursor=cursor, note_id=i)
    #     break
    print(f'{len(ListNotes)}***************2****************')


def Save_note_DB(connection,cursor,note):
    print(f'************* saving data to DB *************')
    temp = (note.my_id, note.full_title, note.full_text, note.my_date)
    temp2 = []
    temp2.append(temp)
    print(temp2)
    cursor.executemany("INSERT INTO Notes_DB VALUES (?,?,?,?)", temp2)
    connection.commit()


def Delete_note_DB(connection,cursor,note_id):
    print(f'************* deleting data to DB *************')
    sql = "DELETE FROM Notes_DB WHERE note_id = ?"
    cursor.execute(sql, (str(note_id),))
    connection.commit()


def Update_note_DB(connection,cursor,note):
    print(f'************* updating data to DB *************')
    temp = (note.full_title, note.full_text, note.my_date, note.my_id)
    print(temp)

    sql = """
    UPDATE Notes_DB
    SET title = ?, content = ?, date = ?
    WHERE note_id = ? 
    """
    cursor.execute(sql, temp)
    connection.commit()


def Get_data_DB(cursor):
    print("************** get data from DB **************")
    sql = "SELECT * from Notes_DB"
    cursor.execute(sql)
    records = cursor.fetchall()
    print("Всего строк:  ", len(records))
    print("Вывод каждой строки")
    print("@@@@@@@@@@@@@@@@ ", a.count_notes)
    if len(records):
        a.count_notes = records[len(records)-1][0]+1
        print("@@@@@@@@@@@@@@@@ ",a.count_notes)
        for row in records:

            print("__________________________________________")
            print("ID:", row[0])
            print("Оглавление:", row[1])
            print("Содержимое:", row[2])
            print("Дата:", row[3])
            print("__________________________________________")
            # update view
            ListNotes.append(Note())
            ListNotes[-1].my_text = ParseShortName(row[2], 10)
            ListNotes[-1].my_title = ParseShortName(row[1], 10)
            ListNotes[-1].full_title = row[1]
            ListNotes[-1].full_text = row[2]
            ListNotes[-1].my_id = row[0]
            ListNotes[-1].my_date = row[3]
            MyLayout.add_widget(ListNotes[-1])
    #cursor.close()


class Screen2(MDScreen):
    """
    Экран редактирования заметки
    """

    def my_back(self, instance):
        """
        кнопка перехода на главный экран
        """
        # existing note
        for note in ListNotes:
            if note.click:
                note.click = False
                if note.full_title != self.ids.Input_Title.text:
                    if not self.ids.Input_Title.text:
                        if self.ids.Input_Body.text:

                            note.my_title = ParseShortName(self.ids.Input_Body.text, 10)
                            note.full_title = note.my_title
                        else:
                            #myApp.select.ids.selection_list.remove_widget(note)
                            ListNotes.remove(note)
                            break
                    else:
                        note.full_title = self.ids.Input_Title.text
                        note.my_title = ""
                        note.my_title = ParseShortName(note.full_title, 10)
                        print(note.my_title)

                note.full_text = self.ids.Input_Body.text
                note.my_text = ParseShortName(self.ids.Input_Body.text, 10)
                note.my_date = str(datetime.datetime.now().date())
                Update_note_DB(connection=connection,
                          cursor=cursor,
                          note=note)

        # new note
        if btnAddNote.click:
            btnAddNote.click = False
            if not self.ids.Input_Title.text and not self.ids.Input_Body.text:  # empty
                ListNotes.remove(ListNotes[-1])
                print(f"Empty Notes, so remove it {len(ListNotes)}")
            else:
                if not self.ids.Input_Title.text:
                    self.ids.Input_Title.text = ParseShortName(self.ids.Input_Body.text, 10)
                a.count_notes += 1
                ListNotes[-1].my_text = ParseShortName(self.ids.Input_Body.text, 10)
                ListNotes[-1].my_title = ParseShortName(self.ids.Input_Title.text, 10)
                ListNotes[-1].full_title = self.ids.Input_Title.text
                ListNotes[-1].full_text = self.ids.Input_Body.text
                ListNotes[-1].my_id = int(a.count_notes)
                ListNotes[-1].my_date = str(datetime.datetime.now().date())
                MyLayout.add_widget(ListNotes[-1])
                Save_note_DB(connection=connection,
                        cursor=cursor,
                        note=ListNotes[-1])
                #Get_data_DB(cursor=cursor)
        sm.switch_to(ScreensList[0])

    def my_delete(self, instance):
        """
        удалить заметку существующую или новую
        """
        temp_list = []
        for i, note in enumerate(ListNotes):
            if note.click:
                note.click = False
                MyLayout.remove_widget(note)
                ListNotes.remove(note)
                break
        print(f"delete note = {note.my_id}")
        if btnAddNote.click:
            btnAddNote.click = False
            ListNotes.remove(ListNotes[-1])
        Delete_note_DB(connection, cursor, note.my_id)
        sm.switch_to(ScreensList[0])
        #Get_data_DB(cursor=cursor)


class myApp(MDApp):
    title = "Notes = py+kivy"
    overlay_color = get_color_from_hex("#6042e4")
    progress_round_color = get_color_from_hex("#ef514b")
    flag_selected = False
    time_1st = 0.0
    time_2nd = 0.0
    count_selection = 0
    count_notes = 0
    item_selection = []
    # global layout
    # layout = None

    def build(self):
        # *****************Экран 1 - список заметок*****************
        global MyLayout, ScreensList, sm, screen_edit_note, screen_main, btnAddNote, main_tool
        # return object
        screen_main = MDScreen(md_bg_color=(.5, .5, .5, 1))
        main_tool = Tool()
        # объект скролл для прокручивания по Y слоя self.layout
        self.scroll = ScrollView()
        # инициализация слоя
        for note in ListNotes:
            MyLayout.add_widget(note)
        # привязка слоя self.layout к объекту скролл
        self.scroll.add_widget(MyLayout)
        # Кнопка - добавить заметку
        btnAddNote = CustomBtn(x=Window.size[0] - 80, y=50)
        # добавляем элементы на главный экран
        screen_main.add_widget(self.scroll)
        screen_main.add_widget(btnAddNote)
        screen_main.add_widget(main_tool)

        # *****************Экран 2 - редактирование заметки*****************
        screen_edit_note = Screen2()

        # *****************Менеджер экранов*****************
        sm = ScreenManager()
        ScreensList.append(screen_main)
        ScreensList.append(screen_edit_note)
        sm.switch_to(ScreensList[0])
        Get_data_DB(cursor)
        # возвращаем текщий экран №1
        return sm


ListNotes = []  # список объектов-иконок
MyLayout = CallNotes()  # пользовательский слой на котором располагаются иконки заметок
ScreensList = []  # список экранов для ScreenManager

# database - CREATE
connection = sqlite3.connect('Garvel_Loken.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Notes_DB
                    (note_id int primary key, title text, content text, date text)
                """)
connection.commit()
#connection.close()

# Главный цикл программы
if __name__ == "__main__":
    print(__name__)
    a = myApp()
    a.run()
