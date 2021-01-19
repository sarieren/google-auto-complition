import glob
import json
import os

dict_id_restart = {}
dict_id_compilation = {}
id_ = 1


def create_dict(startpath):

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        middle_path = os.path.basename(root)
        all_path = startpath + '/'
        if level == 1:
            all_path += middle_path
            all_path += '/'
        if level == 2:
            all_path += 'python-3.8.4-docs-text/'
            all_path += middle_path
            all_path += '/'
        for file_path in files:
            print(all_path + file_path)
            add_query_to_dict(all_path + file_path)

    replace_key_value()

    enter_data_to_json()


def add_query_to_dict(path_):
    with open(path_, encoding="utf8") as file_txt:
        for line in file_txt:
            if (line != "\n" and len(line) > 2):
                add_line_to_dict(line)


def add_line_to_dict(line):
    line = line[:-1]
    list_word = line.split(" ")
    only_alpha_bet = [''.join(e for e in word if e.isalnum()) for word in list_word]
    lower_word = [word.lower() for word in only_alpha_bet if word != ""]

    good_line = " ".join(lower_word)
    global id_
    if not dict_id_restart.get(good_line):
        dict_id_restart[good_line] = id_
        id_ += 1


def replace_key_value():

    for key, value in dict_id_restart.items():
        dict_id_compilation[value] = key


def enter_data_to_json():

    with open('id_restart.json', 'w') as outfile:
        json.dump(dict_id_restart, outfile)
    with open('id_compilation.json', 'w') as outfile:
        json.dump(dict_id_compilation, outfile)


create_dict(r'C:\Users\s0573\Documents\bootcamp\auto complition\data')
