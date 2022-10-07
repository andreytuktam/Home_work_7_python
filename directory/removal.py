

def removal_directory(text_rem):
    count_part = 0
    my_file = open("directory.txt", "r")
    for line in my_file:
        for part in line.split('-'):
            if text_rem in part:
                count_part = count_part + 1
                # print (line)
    my_file.close()
    if count_part == 0:
        print('С такими параметрами поиска - информации нет!')
    if count_part > 0:   
        answer_conclusion = str(input(' -введите номер записи, которую хотите удалить \
            \n -если хотите вернуться в основное меню введите любое значение\n')) + "-" 
        my_file = open("directory.txt", "r")
        for line in my_file:
            for part in line.split(':'):
                if answer_conclusion in part:
                    # print (line)
                    my_file = open("directory.txt", "r")
                    line_rec = my_file.readlines()
                    print(line_rec)
                    my_file.close()
                    my_file = open("directory.txt", "w")
                    for line_2 in line_rec:
                        if line_2 != line:
                            my_file.write(line_2)
                    my_file.close()
                    my_file_2 = open("directory_2.txt", "w")
                    for line_3 in range(len(line_rec)):
                        if line_rec[line_3] != line:
                            s = line_rec[line_3].split(" ")
                            for j in s:
                                my_file_2.write(j + '\n')
                    my_file_2.close()
                    
        
        
       