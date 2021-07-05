from kivy.app import App
from kivy.config import Config

_WIDTH = 400
_HEIGHT = 200
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', _WIDTH)
Config.set('graphics', 'height', _HEIGHT)

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
import requests


API_KEY = 'N2Q1MWFjM2ItZWQzMi00Mjk0LWEyZDQtYTY5YmNmZjgzYzVkOjA2MTEwNmJlN2U2YTRmOWFhYjg0MjBlNDlhM2UyZjI2'
URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
unnecessary = ("the", "and", "was", "were", "not", 'did', 'will', 'had', 'have', 'has',
               'all', 'that', 'this', 'with', 'for', 'from', 'are', 'she', 'they', 'his',
               'then', 'than', 'york', 'crusoe', 'robinzon', 'visa', 'mastercard', 'maestro', 'paypal', 'webmoney', 'qiwi',)
URL_TRANS = 'https://developers.lingvolive.com/api/v1/Minicard'


class Collect:
    def __init__(self):
        self.stat = {}
        self.word = ''

    def collections(self, file_name):
        with open(file_name, 'r', encoding='cp1251') as file:
            self.word = ""
            for line in file:
                for char in line:
                    if 90 >= ord(char) >= 65 or 122 >= ord(char) >= 97:
                        self.word += char
                    elif len(self.word) > 2 and not self.word in unnecessary:
                        if self.word in self.stat:
                            self.stat[self.word] += 1
                        else:
                            self.stat[self.word] = 1
                        self.word = ""
                    elif len(self.word) <= 2:
                        self.word = ""
                    else:
                        self.word = ""
                    self.word = self.word.lower()
            self.collect = list(self.stat.items())
            self.collect.sort(key=lambda x: x[1], reverse=True)
            self.resultTop = [i[0] for i in self.collect]
        return self.resultTop


class Translate:

    def __init__(self, url, key):
        pass
        self.API_KEY = key
        self.URL_AUTH = url
        self.headers = {
            'Authorization': 'Basic ' + self.API_KEY
        }
        self.auth()

    def auth(self):
        token_auth = requests.post(url=self.URL_AUTH, headers=self.headers)
        self.token_status = token_auth.status_code
        if self.token_status == 200:
            self.token = token_auth.text
            print('Token есть можно поесть')

    def translate(self, url, word):
        if self.token_status == 200:
            print('wait')
            header = {'Authorization': 'Bearer ' + self.token}
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1049
            }
            self.order = requests.get(url=url, headers=header, params=params)
            self.result = self.order.json()
            try:
                self.trans_word = self.result['Translation']['Translation']
                # print(self.result)
                print('перевод - ОК')
            except:
                self.trans_word = 'Не найден вариант перевода'
                # print(self.result)
                print('перевод - NOK')
        else:
            self.trans_word = '=== Сервер не отвечает ==='
            print('=== No access ===')


class AL2MS(App):

    def calculate(self, instance):
        file_in = self.in1.text
        file_out = self.in2.text
        self.numb_words = int(self.words.text)

        if 'txt' in file_in and 'txt' in file_out:
            if self.result == []:
                try:
                    self.result = book.collections(file_in)
                except FileNotFoundError:
                    self.result = []
            ##############
            print(self.result[:self.numb_words])
            print(len(self.result))
            ##############
            with open(file_out, 'w', encoding='cp1251') as file:
                print('создаем файл перевода')
                for word in enumerate(self.result[:self.numb_words]):
                    trans.translate(url=URL_TRANS, word=word[1])
                    my_string = f'{word[0] + 1}) {word[1]}              ' \
                                f'{trans.trans_word}    \n'
                    file.write(my_string)
            print('============== Done ==============')

    def myUpdate(self,instance,value):
        self.result=[]

        if '.txt' in value:
            print('User focused', instance, value)
            try:
                self.result = book.collections(value)
            except FileNotFoundError:
                self.result = []
            self.totalWords.text = str(len(self.result))
        else:
            self.totalWords.text = '0'

    def myUpdateText(self,instance,value):
        try:
            self.numb_words = int(value)
        except:
            self.numb_words = 0
        print(self.result[:self.numb_words])

    def build(self):
        main_widget = Widget()
        self.in1 = TextInput(text='Введите путь до книги...',
                             pos=(0, 170),
                             width=400,
                             height=30)
        self.in1.bind(text=self.myUpdate)
        self.in2 = TextInput(text='Введите путь сохранения файла...',
                             pos=(0, 140),
                             width=400,
                             height=30)
        text1 = Label(text='Выбрано слов:',
                      pos=(10, 110),
                      color=[1, 0, 0, 1],
                      width=100,
                      height=30)
        text2 = Label(text='из:',
                      pos=(220, 110),
                      color=[1, 0, 0, 1],
                      width=100,
                      height=30)
        self.words = TextInput(text='0',
                               halign='center',
                               pos=(130, 110),
                               width=100,
                               height=30)
        self.words.bind(text=self.myUpdateText)
        self.totalWords = Label(text='0',
                                    halign='center',
                                    pos=(300, 110),
                                    width=100,
                                    height=30)
        btn_start = Button(text='Старт',
                           background_color=[0.5, 0.5, 1, 1],
                           pos=(0, 0),
                           width=100,
                           height=50,
                           on_press=self.calculate)
        main_widget.add_widget(self.in1)
        main_widget.add_widget(self.in2)
        main_widget.add_widget(text1)
        main_widget.add_widget(text2)
        main_widget.add_widget(self.words)
        main_widget.add_widget(self.totalWords)
        main_widget.add_widget(btn_start)
        return main_widget


if __name__ == '__main__':
    book = Collect()
    trans = Translate(URL_AUTH, API_KEY)
    ARZAMAS = AL2MS().run()
