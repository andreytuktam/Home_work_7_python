

def view_directory():
    my_file = open("directory.txt", "r")
    for line in my_file:
        print (line)
    my_file.close()
