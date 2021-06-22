import requests, json

API_KEY = 'N2Q1MWFjM2ItZWQzMi00Mjk0LWEyZDQtYTY5YmNmZjgzYzVkOjA2MTEwNmJlN2U2YTRmOWFhYjg0MjBlNDlhM2UyZjI2'
URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
# headers_auth = {'Authorization': 'Basic ' + API_KEY}
#
# token_auth = requests.post(url=URL_AUTHENTICATE, headers=headers_auth)
# token = token_auth.text
#
# print(token_auth.status_code)
# print(token)
#
url = 'https://developers.lingvolive.com/api/v1/Minicard'
# params = {
#     'text': 'always',
#     'srcLang': 1033,
#     'dstLang': 1049
# }
# head = {'Authorization': 'Bearer ' + token}
# s = requests.get(url=url, headers=head, params=params)
# res = s.json()
# print(res['Translation']['Translation'])


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


    def translate(self, url, word):
        if self.token_status == 200:
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
            except:
                self.trans_word = 'Не найден вариант перевода'
                #print(self.result)
        else:
            self.trans_word = 'Сервер не отвечает'

t = Translate(URL_AUTH, API_KEY)
while True:
    word = input()
    t.translate(url, word)
    print(t.trans_word)