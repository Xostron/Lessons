
import os
import time

_DATA = 2
_TIME = 3
_CURSOR_VALUE = 5
# file_name = input('Enter path to file...\n')

def ProcessFile(file_name, my_dir, ori_file_name, count_files):
    global curr_numb
    #print('Start...')
    start = time.time()
    # открываем файл с исходными данными
    with open(file_name, 'r', encoding='cp1251') as file:
        count = 0
        for line in file:
            count += 1
            if count == 1:  # читаем тэги
                line = line.replace('\n','')
                tagname = [signal.replace('.PV', '_PV_') for signal in line.split(',') if '.PV' in signal]
                # создаем папку Result
                path_result = f'{my_dir}\Result'
                try:
                    os.mkdir(path_result)
                except:
                    pass
                file_list = []
                j = 0
                # создаем файлы
                files_directory_result = [i for i in os.listdir(path_result) if '.csv' in i]
                for tag in enumerate(tagname):
                    file_csv = tag[1] + 'Value.csv'
                    if not file_csv in files_directory_result:
                        file_list.append(open(f'{path_result}/{file_csv}', mode="a", encoding='utf-8'))
                    else:
                        file_csv = f'{tag[1]}Value_{ori_file_name}.csv'
                        file_list.append(open(f'{path_result}/{file_csv}', mode="a", encoding='utf-8'))
                #print('Tagname: ', tagname)
            elif count > 7: # обработка данных, начинается во всех документах с 8 строки
                row = [i for i in line.split(',')]
                #print('Извлекаемые данные: ', row)
                sensor_row = ''

                for tag in enumerate(tagname):
                    # file_csv = tag[1] + 'Value.csv'
                    # print('Имя файла ', file_csv)
                    sensor_row += row[_DATA].replace('-','/') + " "
                    sensor_row += row[_TIME] + ','
                    sensor_row += '192,,'
                    sensor_row += row[_CURSOR_VALUE + tag[0]].replace('\n', '') + '\n'
                    #print('Запись: ', sensor_row)
                    file_list[tag[0]].write(sensor_row)
                    sensor_row = ''
    end = time.time()  # ========конец обработки исходного файла============
    elapsed = round(end - start, 6)
    curr_numb += 1
    # закрываем файлы в папке Result
    for file in file_list:
        file.close()
    print(f'Finish file {curr_numb} of {count_files}..., {elapsed} sec')


#############################main##########################################
path = input('enter path to directory...')
print('=================================Start=================================')
prg_start = time.time()
try:
    files_directory = [i for i in os.listdir(path) if '.csv' in i]
    files_name = [f"{path}\{i}" for i in files_directory]
    # print(files_directory)
    # print(files_name)
    count_files = len(files_name)
    print(f"Количество файлов {count_files}")

except:
    pass

curr_numb = 0
for i in enumerate(files_name):
    ProcessFile(i[1],path,files_directory[i[0]], count_files)

prg_finish = time.time()
prg_elapsed = round(prg_finish - prg_start, 6)
print(f'=================================Finish================================={prg_elapsed} sec')
input()










