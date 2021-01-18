from completion import *


def output_(text):
    print(text)


def input_():

    text = input('The system is ready. Enter your text: ')
    while True:

        list_word = text.split(" ")
        only_alpha_bet = [''.join(e for e in word if e.isalnum()) for word in list_word]
        lower_word = [word.lower() for word in only_alpha_bet]

        res = completion(" ".join(lower_word))

        output_("HERE are " + str(len(res)) + " suggestions")
        for i in range(len(res)):
            output_(str(i+1) + ". " + res[i].completed_sentence)

        if text.endswith("#"):
            break

        text += input(text)

    input_()


if __name__ == '__main__':
    input_()