

def view_directory_2():
    my_file = open("directory_2.txt", "r")
    for line in my_file:
        if "-" in line: 
            print (line)
        if "-" not in line: 
            print (line)
    my_file.close()