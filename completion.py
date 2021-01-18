import json

from Rep_Del_Add import *


def get_id():

    with open(r'C:\Users\s0573\Documents\bootcamp\auto complition\id_compilation.json', 'r') as file:
        data_ = json.load(file)
    return data_


def load_data():
    with open("data.json", 'r') as file:
        data_ = json.load(file)
    return data_


data = load_data()
id_completion = get_id()


class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score


def completion(sentence):

    res = []
    count = 0

    if data.get(sentence, 0):
        values = data[sentence]
        for key, value in values.items():
            count += 1
            res.append(convert_to_auto_completed(sentence, key, value))

    if count < 5:
        mashu = replace(count, sentence, data)
        for m in mashu:
            count += 1
            res.append(convert_to_auto_completed(m[0], m[1], m[2]))

    if count< 5:
        mashu = delete_(count, sentence, data)
        for m in mashu:
            count += 1
            res.append(convert_to_auto_completed(m[0], m[1], m[2]))

    if count< 5:
        mashu = add_(count, sentence, data)
        for m in mashu:
            count += 1
            res.append(convert_to_auto_completed(m[0], m[1], m[2]))

    return res


def convert_to_auto_completed(sentence, key, value):

    sentence_key = " "
    if(id_completion.get(key)):
        sentence_key = id_completion[key]
    auto = AutoCompleteData(sentence_key, sentence, value[0], value[1])
    return auto


