

def conclusion_directory(text_find):
    count_part = 0
    my_file = open("directory.txt", "r")
    for line in my_file:
        for part in line.split(' '):
            if text_find in part:
                count_part = count_part + 1
                print(part, end =" ")
    print('')
    if count_part == 0:
        print('С такими параметрами поиска - информации нет!')
    my_file.close()
    
    
    


    
        