import requests, json


# data = {'source': 'ленточный конвейер'}
# s = requests.get(r'https://fasttranslator.herokuapp.com/api/v1/detect', params=data)
# data = s.json()
# print(data['Lang'])
#
#
#
# url_post = 'https://fasttranslator.herokuapp.com/api/v1/text/to/text'
# data_post = {
#     'source': 'allure',
#     'lang': 'en-ru'
# }
# r = requests.post(url=url_post, data=data_post)
#
# out = r.json()
# print(out)


# u = 'https://translate.yandex.ru/?utm_source=wizard&lang=ru-en&text=привет'
# https://translate.yandex.ru/?utm_source=wizard&lang=ru-en
# https://translate.yandex.ru/?utm_source=wizard&lang=ru-en
# &text=привет%20меня%20зовут
u1 = 'https://translate.yandex.ru/?utm_source=wizard&lang=ru-en&text=привет%20меня%20зовут'
s = requests.get(u1)
print(s.text.encode('utf-8'))

