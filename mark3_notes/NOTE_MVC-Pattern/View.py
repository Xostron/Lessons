from kivymd.app import MDApp
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDIconButton, MDFloatingActionButton
from kivy.uix.scrollview import ScrollView
import datetime
import time
import Controller


class CallNotes(MDGridLayout):
    """
    Layout for class Note
    """
    pass


class Tool(MDScreen):
    """
    Toolbar for main screen
    """
    pass


class Note(MDFloatLayout):
    """
    icon Notes
    """

    def __init__(self, class_controller, **kwargs):
        """
        constructor of class
        Controller: class View is part of class Controller
        """
        super(Note, self).__init__(**kwargs)
        self.click = False
        self.selected = False
        self.help_selected = False
        self.flag_reaction = False
        self.Controller = class_controller

    def Helper_CSF(self, instance):
        """
        auxiliary function for process event press_on
        """
        self.Controller.View.time_1st = time.time()
        self.help_selected = True
        print(f"нажата заметка - Helper {self.Controller.View.time_1st}")
        for i in self.Controller.View.List_notes:
            if i.help_selected:
                i.help_selected = False
                self.obj = i
                break
        # print(dir(obj)) # позволяет увидеть все поля объекта
        if not self.Controller.View.flag_selected:
            self.anim = Animation(
                my_angle=360,
                d=self.obj.my_delay,
                t="in_sine", )
            self.anim.start(self.obj)
            self.my_color_circle_outer = (.3, .5, .8, 1)

    def Create_select_func(self, instance):
        """
        Event note press_on
        """
        self.Controller.View.time_2nd = time.time()
        time_res = round(self.Controller.View.time_2nd - self.Controller.View.time_1st, 2)
        print(f"Нажата заметка - Create_Select_func {time_res}")
        if not self.Controller.View.flag_selected:
            # если нет выделенных заметок
            if time_res >= self.my_delay:
                self.Controller.View.flag_selected = True  # есть выделенные заметки
            else:
                # не выделяем текущую заметку
                self.my_color_circle_outer = (.7, .7, .7, 1)
                self.anim.cancel_all(self.obj, 'my_angle')
                self.my_angle = 0
            if time_res >= self.my_reaction and time_res <= self.my_delay:
                self.flag_reaction = True
        if not self.Controller.View.flag_selected:
            if not self.flag_reaction:
                # если нет выделенных заметок
                print(f"Click on note - ++++++{self.Controller.View.flag_selected}", instance)
                self.Controller.View.SE.ids.Input_Title.text = self.full_title
                self.Controller.View.SE.ids.Input_Body.text = self.full_text
                self.Controller.View.Manager.switch_to(self.Controller.View.manager_list[1])
                self.click = True
            else:
                self.flag_reaction = False
        elif not self.selected:
            # если есть выделенные заметки и текущая заметка не выделена
            self.selected = True
            self.Controller.View.count_selection += 1
            self.Controller.View.item_selection.append(self.my_id)
            self.my_color_circle_outer = (.3, .5, .8, 1)
            self.my_angle = 0
            self.md_bg_color = (.3, .5, .8, 1)
            print(f"Количество выбранных = {self.Controller.View.count_selection}")
        else:
            self.selected = False
            self.md_bg_color = (.7, .7, .7, 1)
            self.Controller.View.count_selection -= 1
            self.Controller.View.item_selection.remove(self.my_id)
            for i in self.Controller.View.List_notes:
                if i.selected:
                    self.Controller.View.flag_selected = True
                    break
                else:
                    self.Controller.View.flag_selected = False

        if self.Controller.View.flag_selected:
            self.Controller.View.SM_tool.ids.tool_bar.left_action_items = [
                ["close", lambda x: Unselected_all(self.Controller), ]]
            self.Controller.View.SM_tool.ids.tool_bar.right_action_items = [
                ["trash-can", lambda x: Delete_selected(self.Controller), ],
                ["dots-vertical"]]
            self.Controller.View.SM_tool.ids.tool_bar.title = f"{self.Controller.View.count_selection}"
        else:
            self.Controller.View.SM_tool.ids.tool_bar.left_action_items = [['']]
            self.Controller.View.SM_tool.ids.tool_bar.right_action_items = [['']]
            self.Controller.View.SM_tool.ids.tool_bar.title = "Notes"


class CustomBtn(MDFloatingActionButton):
    """кнопка - создать заметку"""

    def __init__(self, class_controller, **kwargs):
        super(CustomBtn, self).__init__(**kwargs)
        self.click = False
        self.Controller = class_controller

    def add_note(self, instance):
        """
        create note
        """
        # добавление заметки на слой
        self.Controller.View.List_notes.append(Note(class_controller=self.Controller))
        self.Controller.View.Manager.switch_to(self.Controller.View.manager_list[1])
        self.Controller.View.SE.ids.Input_Title.text = ''
        self.Controller.View.SE.ids.Input_Body.text = ''
        self.click = True
        for note in self.Controller.View.List_notes:
            note.selected = False
            note.md_bg_color = (.7, .7, .7, 1)
        self.Controller.View.count_selection = 0
        self.Controller.View.flag_selected = False


class Screen2(MDScreen):
    """
    Edit Screen note
    """

    def __init__(self, class_controller, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.Controller = class_controller

    def my_back(self, instance):
        """
        return back to Main Screen
        """
        # existing note
        for note in self.Controller.View.List_notes:
            if note.click:
                note.click = False
                if note.full_title != self.ids.Input_Title.text:
                    if not self.ids.Input_Title.text:
                        if self.ids.Input_Body.text:

                            note.my_title = ParseShortName(self.ids.Input_Body.text, 10)
                            note.full_title = note.my_title
                        else:
                            self.Controller.View.List_notes.remove(note)
                            break
                    else:
                        note.full_title = self.ids.Input_Title.text
                        note.my_title = ""
                        note.my_title = ParseShortName(note.full_title, 10)
                        print(note.my_title)

                note.full_text = self.ids.Input_Body.text
                note.my_text = ParseShortName(self.ids.Input_Body.text, 10)
                note.my_date = str(datetime.datetime.now().date())
                self.Controller.update_DB(note)

        # new note
        if self.Controller.View.SM_btn_creator.click:
            self.Controller.View.SM_btn_creator.click = False
            if not self.ids.Input_Title.text and not self.ids.Input_Body.text:  # empty
                self.Controller.View.List_notes.remove(self.Controller.View.List_notes[-1])
                print(f"Empty Notes, so remove it {len(self.Controller.View.List_notes)}")
            else:
                if not self.ids.Input_Title.text:
                    self.ids.Input_Title.text = ParseShortName(self.ids.Input_Body.text, 10)
                self.Controller.View.count_notes += 1
                self.Controller.View.List_notes[-1].my_text = ParseShortName(self.ids.Input_Body.text, 10)
                self.Controller.View.List_notes[-1].my_title = ParseShortName(self.ids.Input_Title.text, 10)
                self.Controller.View.List_notes[-1].full_title = self.ids.Input_Title.text
                self.Controller.View.List_notes[-1].full_text = self.ids.Input_Body.text
                self.Controller.View.List_notes[-1].my_id = int(self.Controller.View.count_notes)
                self.Controller.View.List_notes[-1].my_date = str(datetime.datetime.now().date())
                self.Controller.View.SM_layout_note.add_widget(self.Controller.View.List_notes[-1])
                self.Controller.save_to_DB(self.Controller.View.List_notes[-1])

        self.Controller.View.Manager.switch_to(self.Controller.View.manager_list[0])

    def my_delete(self, instance):
        """
        Button deleting note on toolbar of screen edit
        """
        temp_list = []
        for i, note in enumerate(self.Controller.View.List_notes):
            if note.click:
                note.click = False
                self.Controller.View.SM_layout_note.remove_widget(note)
                self.Controller.View.List_notes.remove(note)
                break

        if self.Controller.View.SM_btn_creator.click:
            self.Controller.View.SM_btn_creator.click = False
            self.Controller.View.List_notes.remove(self.Controller.View.List_notes[-1])
        self.Controller.del_note_DB(note.my_id)
        self.Controller.View.Manager.switch_to(self.Controller.View.manager_list[0])


class View():
    """
    main class
    """
    title = "Notes = py+kivy"
    overlay_color = get_color_from_hex("#6042e4")
    progress_round_color = get_color_from_hex("#ef514b")
    flag_selected = False
    time_1st = 0.0
    time_2nd = 0.0
    count_selection = 0
    count_notes = 0
    item_selection = []

    def __init__(self, class_controller, **kwargs):

        super(View, self).__init__(**kwargs)

        self.Controller = class_controller
        self.List_notes = []

        # *****************Экран 1 - Главный экран (SM - Screen main)*****************
        self.SM = MDScreen(md_bg_color=(.5, .5, .5, 1))
        self.SM_tool = Tool()
        # объект скролл для прокручивания по Y слоя self.layout
        self.SM_scroll = ScrollView()
        # инициализация слоя
        self.SM_layout_note = CallNotes()
        for note in self.List_notes:
            self.SM_layout_note.add_widget(note)
        # привязка слоя self.layout к объекту скролл
        self.SM_scroll.add_widget(self.SM_layout_note)
        # Кнопка - добавить заметку
        self.SM_btn_creator = CustomBtn(x=Window.size[0] - 80, y=50, class_controller=self.Controller)
        # добавляем элементы на главный экран
        self.SM.add_widget(self.SM_scroll)
        self.SM.add_widget(self.SM_btn_creator)
        self.SM.add_widget(self.SM_tool)

        # *****************Экран 2 - редактирование заметки (SE - Screen edit)*****************
        self.SE = Screen2(class_controller=self.Controller)

        # *****************Менеджер экранов*****************
        self.manager_list = []
        self.Manager = ScreenManager()
        self.manager_list.append(self.SM)
        self.manager_list.append(self.SE)
        self.Manager.switch_to(self.manager_list[0])

        # *****************First init from DB*****************
        self.update_note(self.Controller)

    def update_note(self, class_controller):
        """
        функция обновления экрана с заметками, use as first init
        class_controller - объект приложения из Controller.py

        data: текст заметки из БД
        List_notes: список объектов заметок
        SM_layout_note: объект слой для вывода заметок
        """
        data = class_controller.get_from_DB()
        if len(data):
            self.count_notes = data[len(data) - 1][0] + 1
            print("@@@@@@@@@@@@@@@@ ", self.count_notes)
            for row in data:
                print("__________________________________________")
                print("ID:", row[0])
                print("Оглавление:", row[1])
                print("Содержимое:", row[2])
                print("Дата:", row[3])
                print("__________________________________________")
                self.List_notes.append(Note(class_controller))
                self.List_notes[-1].my_text = ParseShortName(row[2], 10)
                self.List_notes[-1].my_text = ParseShortName(row[2], 10)
                self.List_notes[-1].my_title = ParseShortName(row[1], 10)
                self.List_notes[-1].full_title = row[1]
                self.List_notes[-1].full_text = row[2]
                self.List_notes[-1].my_id = row[0]
                self.List_notes[-1].my_date = row[3]
                self.SM_layout_note.add_widget(self.List_notes[-1])

# чтение структурного файла .kv
with open(file="elements.kv", encoding="utf-8") as KV:
    Builder.load_string(KV.read())
Window.size = (350, 600)


def ParseShortName(ori, length):
    """
    Работа со строкой:
    - ограничение исходной строки до кол-ва символов length
    - ограничение строки до символа "перенос каретки"

    ori: исходный текст
    length: максимальное количество символов в результате res
    """
    res = ''
    for i in ori[:length]:
        if i != '\n':
            res += i
        else:
            break
    res += "..."
    return res


def Unselected_all(class_controller):
    """
    Снятие выделения заметок по кнопке на панели меню
    """
    for i in class_controller.View.List_notes:
        i.selected = False
        i.md_bg_color = (.7, .7, .7, 1)
    class_controller.View.flag_selected = False
    class_controller.View.count_selection = 0
    class_controller.View.SM_tool.ids.tool_bar.left_action_items = [['']]
    class_controller.View.SM_tool.ids.tool_bar.right_action_items = [['']]
    class_controller.View.SM_tool.ids.tool_bar.title = "Notes"


def Delete_selected(class_controller):
    """
    Удаление заметки с экрана и БД
    class_controller - объект приложения из Controller.py

    item_selection: список индексов заметок для удаления из БД
    List_notes: список объектов заметок
    SM_layout_note: объект слой для вывода заметок
    """
    print(f'{len(class_controller.View.List_notes)}***************1****************')
    # цикл удаления заметки с виджета и из списка заметок
    for note in class_controller.View.List_notes[len(class_controller.View.List_notes)::-1]:
        if note.selected:
            print(f'delete - {note.selected}')
            class_controller.View.SM_layout_note.remove_widget(note)
            class_controller.View.List_notes.remove(note)
    Unselected_all(class_controller)
    print('@@@@@ deleting list ', class_controller.View.item_selection)
    # цикл удаления заметок из БД
    for i in class_controller.View.item_selection:
        print('check deleting', i, type(i))
        class_controller.del_note_DB(i)
    print(f'{len(class_controller.View.List_notes)}***************2****************')



