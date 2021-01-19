import glob
import json
import os


def get_id():

    with open(r'C:\Users\s0573\Documents\bootcamp\auto complition\id_restart.json', 'r') as file:
        data = json.loads(file.read())
    return data


path_data = r'C:\Users\s0573\Documents\bootcamp\auto complition\data'
dict_data = {}
dict_id = get_id()

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def create_dict(path_):
    files = glob.glob(os.path.join(path_,  '*.txt'))

    for file in files:
        if file.endswith(".txt"):
            print(file)
            add_query_to_dict(file)
        else:
            create_dict(file)

    enter_data_to_json()


def add_query_to_dict(path_):
    with open(path_, encoding="utf8") as file_txt:
        for line in file_txt:
            if(line != "\n" and len(line) > 2):
                add_line_to_dict(line)


def add_line_to_dict(line):
    line = line[:-1]
    list_word = line.split(" ")
    only_alpha_bet = [''.join(e for e in word if e.isalnum()) for word in list_word]
    lower_word = [word.lower() for word in only_alpha_bet if word != ""]

    good_line = " ".join(lower_word)

    slice_by_char = []
    sof = max(len(good_line) + 1, 10)
    for i in range(1, sof):
        res = get_slice_by_char(i, good_line)
        if res:
            slice_by_char.append(get_slice_by_char(i, good_line))

    slice_by_char.append(good_line)

    for word in slice_by_char:
        score = get_score(word, good_line, 0)
        offset = get_offset(word, good_line)
        add_data(good_line, word, offset, score)


def get_slice_by_char(i, good_line):
    if good_line[i - 1] != " ":
        return good_line[:i]
    else:
        return 0


def get_score(words, sentence, del_or_irrel):
    i = 0

    while i < len(words) and i < len(sentence) and words[i] == sentence[i]:
        i += 1

    score = (len(words) - 1) * 2

    if not del_or_irrel:
        if i < 4:
            score = score - (5 - i)
        else:
            score -= 1

    if del_or_irrel:
        if i < 4:
            score = score - (10 - (2*i))
        else:
            score -= 2

    return score


def get_offset(words, sentence, from_delete_or_irrl = 0):

    i = 0

    if from_delete_or_irrl == 1:
        while (i < len(words) and i < len(sentence) )and (words[0] != sentence[i] or words[i] == " "):
            i += 1
    elif from_delete_or_irrl == 2:
        while (i < len(words) and i < len(sentence)) and (words[i] != sentence[0] or words[i] == " "):
            i += 1
    else:
        while (i < len(words) and i < len(sentence) )and (words[i] != sentence[i] or words[i] == " "):
            i += 1
    return i


def add_data(seq, sub_seq, offset, score):

    seq_id = dict_id[seq]

    if dict_data.get(sub_seq, 0):

        if not dict_data.get(sub_seq).get(seq_id, 0):
            if(len(list(dict_data[sub_seq].values()))< 5):
                dict_data[sub_seq][seq_id] = [offset, score]
            else:
                min_ = score
                to_delete = None
                if(dict_data != {}):

                    for key, value in dict_data.get(sub_seq).items():
                        if(value[1] < score):
                            to_delete = key
                            min_ = value[1]
                    if to_delete:
                        del dict_data[sub_seq][key]
                        dict_data[sub_seq][seq_id] = [offset, score]

    else:

        dict_data[sub_seq] = {seq_id: [offset, score]}


def enter_data_to_json():
    with open('data.json', 'w') as outfile:
        json.dump(dict_data, outfile)


create_dict( r'C:\Users\s0573\Desktop\archive')




