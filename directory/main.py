

import record as rec
import conclusion as con       
import view
import view_2
import removal  


def start():
    flag = True
    count_record = 0
    while flag == True:
        answer = str(input('Телефонный справочник:\n -введите "1" для внесения новой записи \
            \n -введите "2" для поиска\n -введите "3" для просмотра содержимого \
                \n -введите "4" для удаления записи\n -введите "0" для выхода из программы\n'))
        if answer == '0':
            flag = False
        if answer == '1':
            count_record += 1
            text_new = (str(input("Введите имя:\n"))\
                + " " + str(input("Введите номер телефона:\n"))\
                    + " " + str(input("Введите описание:\n")))
            rec.record_directory(text_new, count_record)
        if answer == '2':
            text_find = str(input("Для поиска ведите имя:\n"))
            print("")
            con.conclusion_directory(text_find) 
        if answer == '3':
            answer_2 = str(input(' -введите "1" для просмотра в формате строки \
                \n -введите "2" для просмотра в формате столбца\n'))
            if answer_2 == '1':   
                view.view_directory()
            if answer_2 == '2':
                view_2.view_directory_2()
        if answer == '4':
            text_rem = str(input("Для удаления ведите имя:\n"))
            print("")
            removal.removal_directory(text_rem) 
start()