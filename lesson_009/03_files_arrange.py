# -*- coding: utf-8 -*-

import os, time, shutil, zipfile

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
# for dirpath, dirnames, filenames in os.walk(path):
#     print(dirpath, dirnames, filenames)
# TODO здесь ваш код

path_file = r'D:\ASKAR\test\icons.zip'
extract_path = r'D:\ASKAR\test\icons'


def unzip(path_file, extract_path):

    zfile = zipfile.ZipFile(path_file, 'r')  # инициализируем наш целевой icons.zip как объект
    for filename in zfile.namelist():  # цикл по файлам в icons.zip
        # print("1) ", os.path.normpath(filename))
        #print('2)',zfile.getinfo(filename).date_time)
        # print('3)', zfile.getinfo(filename))
        if 'png' or 'jpg' or 'gif' in zfile.getinfo(filename):
            #print('I find you, letherman')
            rawTime = zfile.getinfo(filename).date_time
            month = rawTime[1]
            #day = rawTime[2]
            year = rawTime[0]
            collect_path = extract_path + rf'\{year}\{month}'
            print(collect_path)
        #break
        #data_time = time.gmtime(raw_time)

        #print(collect_path)
        try:
            os.makedirs(collect_path)
        except OSError:
            print("Creation of the directory %s failed" % collect_path)
            zfile.extract(filename, path=collect_path)
        else:
            print("Successfully created the directory %s" % collect_path)
            zfile.extract(filename, path=collect_path)

unzip(path_file, extract_path)
# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
