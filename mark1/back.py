import time, requests, json

API_KEY = 'N2Q1MWFjM2ItZWQzMi00Mjk0LWEyZDQtYTY5YmNmZjgzYzVkOjA2MTEwNmJlN2U2YTRmOWFhYjg0MjBlNDlhM2UyZjI2'
URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
unnecessary = ("the", "and", "was", "were", "not", 'did', 'will', 'had', 'have', 'has',
               'all', 'that', 'this', 'with', 'for', 'from', 'are', 'she', 'they', 'his',
               'then', 'than', 'york', 'crusoe', 'robinson')
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
            'Authorization':'Basic '+ self.API_KEY
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
                #print(self.result)
                print('перевод - ОК')
            except:
                self.trans_word = 'Не найден вариант перевода'
                #print(self.result)
                print('перевод - NOK')
        else:
            self.trans_word = '=== Сервер не отвечает ==='
            print('=== No access ===')


book = Collect()
file_name = input("ведите путь книги: \n")

try:
    result = book.collections(file_name)
except FileNotFoundError:
    result = []

print(result[:100])


trans = Translate(URL_AUTH, API_KEY)

myFile = input('Введите новое имя файла (*****.txt)')
with open(myFile, 'w', encoding='cp1251') as file:
    print('создаем файл перевода')
    for word in enumerate(result[:100]):
        started_at = time.time()  # ====================
        trans.translate(url=URL_TRANS, word=word[1])
        time.sleep(0.6)
        my_string = f'{word[0]+1}) {word[1]}              ' \
                    f'{trans.trans_word}    \n'
        file.write(my_string)
        ended_at = time.time()  # ====================
        elapsed = round(ended_at - started_at, 6)  # ====================
        print(elapsed)
print('============== Done ==============')