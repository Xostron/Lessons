# -*- coding: utf-8 -*-

# (if/elif/else)
import datetime
# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
days = 0
_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# TODO здесь ваш код
if month<12 and month>=1:
    days = _DAYS_IN_MONTH[month]
    print(f"В месяце №{month} - {days} дней")

else:
    print(f"Месяц №{month} не существует.")