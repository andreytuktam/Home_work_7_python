

def record_directory(text_new, count_record):
    
    my_file = open("directory.txt", "a")
    my_file.write(str(count_record) + "-" + text_new + '\n')
    my_file.close()
    
    my_file_2 = open("directory_2.txt", "a")
    my_file_2.write(str(count_record))
    for i in text_new.split(' '):
        my_file_2.write("-" + i + "\n")
    my_file_2.write('\n')
    my_file_2.close()
    
    