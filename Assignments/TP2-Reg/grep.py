import sys
import os
import re

def scan_directory(dir):
    file_list = []
    if re.search("\..*", dir):
        return [dir]
    if os.path.isdir(dir):
        for root, dirs, file in os.walk(dir):
            if len(file) != 0:
                for i in range(len(file)):
                    root = root.replace("\\", "/")
                    file_list.append(f"{root}/{file[i]}")
    else:
        print(f"{dir} not found.")
        quit()
    return file_list

def scan_lines(arg, string, file):
    if string.count("*") == 1:
        string = string.replace("*", ".*")
    elif string.count("*") > 1:
        print("Argument not valid.")
        quit()

    if arg == "":
        current_file = open(file, "r")
        current_file_lines = current_file.read().split("\n")
        for i in range(len(current_file_lines)):
            if re.search(string, current_file_lines[i]):
                line_number_str = (f"Line {i+1}")
                print(f"{file:<40s} {line_number_str:<10s} {current_file_lines[i]:<.40s}")
        current_file.close()
    elif arg == "-i":
        current_file = open(file, "r")
        current_file_lines = current_file.read().split("\n")
        for i in range(len(current_file_lines)):
            if re.search(string, current_file_lines[i], re.I):
                line_number_str = (f"Line {i+1}")
                print(f"{file:<40s} {line_number_str:<10s} {current_file_lines[i]:<.40s}")
        current_file.close()

def scan_words(arg, string, file):
    if string.count("*") == 1:
        string = string.replace("*", ".*")
        string = "^" + string + "$"
    elif string.count("*") > 1:
        print("Argument not valid.")
        quit()
    current_file = open(file, "r")
    current_file_lines = current_file.read().split("\n")
    current_file_words = []
    for i in range(len(current_file_lines)):
        current_file_words.append(current_file_lines[i].split(" "))
    for i in range(len(current_file_lines)):
        for j in range(len(current_file_words[i])):
            if re.search(string, current_file_words[i][j]):
                line_number_str = (f"Line {i+1}")
                print(f"{file:<40s} {line_number_str:<10s} {current_file_lines[i]:<.40s}")

if len(sys.argv) == 4:
    if sys.argv[1] == "-w" or sys.argv[1] == "-i":
        argument = sys.argv[1]
        string_match = sys.argv[2]
        directory = sys.argv[3]
    else:
        print("Argument not valid.")
        quit()
elif len(sys.argv) == 3:
    argument = ""
    string_match = sys.argv[1]
    directory = sys.argv[2]
else:
    print("Argument not valid.")
    quit()

file_list = scan_directory(directory)

if argument == "":
    for file in file_list:
        scan_lines(argument, string_match, file)

elif argument == "-w":
    for file in file_list:
        scan_words(argument, string_match, file)

elif argument == "-i":
    for file in file_list:
        scan_lines(argument, string_match, file)