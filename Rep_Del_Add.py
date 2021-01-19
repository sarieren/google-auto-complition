
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


matching_letters = {
                        'a':['a','q','w','s','x','z'],
                        'b':['b','v','g','h','n'],
                        'c':['c','x','d','f','v'],
                        'd':['d','s','e','r','f','c','x','w'],
                        'e':['e','w','s','d','r'],
                        'f':['f','d','r','t','g','v','c'],
                        'g':['g','f','t','y','h','b','v','r'],
                        'h':['h','g','t','y','u','j','n','b'],
                        'i':['i','u','j','k','l','o'],
                        'j':['j','h','y','u','i','k','m','n'],
                        'k':['k','j','u','i','o','k','m','n'],
                        'l':['l','o','p','k'],
                        'm':['m','k','j','n'],
                        'n':['n','m','j','h','b'],
                        'o':['o','p','l','i','k'],
                        'p':['p','o','l'],
                        'q':['q','w','s','a'],
                        'r':['r','e','d','f','t','g'],
                        's':['s','w','e','d','x','z','a'],
                        't':['t','r','y','g','f'],
                        'u':['u','y','h','j','k','i'],
                        'v':['v','c','b','g','f'],
                        'w':['w','q','a','s','e','d'],
                        'x':['x','z','s','d','c'],
                        'y':['y','t','g','h','j','u'],
                        'z':['z','a','s','x']
                    }


def get_match(values, count, i, temp, del_or_add):
    res = []

    for key, value in values.items():
        if count < 5:
            count += 1

            if i > 4:
                value[1] -= 1
            else:
                if not del_or_add:
                    value[1] = value[1] - (5 - i)
                else:
                    value[1] = value[1] - (10 - (2 * i))

            res.append([temp, key, value])
        else:
            break
    return res



def replace(count, sentence, data):

    res = []
    for i in range(len(sentence)-1, 0, -1):
        if sentence[i] != " " and count < 5:
            for ot in matching_letters[sentence[i]]:
                if ot != sentence[i] and count < 5:
                    temp = sentence[:i] + ot + sentence[i+1:]

                    if data.get(temp, 0):
                        values = data[temp]
                        res.extend(get_match(values, count, i, temp, 0))

                elif count == 5:
                    break
            if count == 5:
                break
        elif count == 5:
            break


    if count < 5:
        for ot in matching_letters[sentence[0]]:
            if ot != sentence[0] and count < 5:
                temp = ot + sentence[1:]

                if data.get(temp, 0):
                    values = data[temp]
                    res.extend(get_match(values, count, 0, temp, 0))

            elif count == 5:
                break

    return res


def delete_(count, sentence, data):

    res = []
    for i in range(len(sentence)-1, 0, -1):
        if sentence[i] != " " and count < 5:
            temp = sentence[0:i] + sentence[i + 1:]
            if (len(temp) > 1):
                    if data.get(temp, 0):
                        values = data[temp]
                        res.extend(get_match(values, count, i, temp, 1))

            if count == 5:
                break
        elif count == 5:
            break

    if count < 5:
        temp = sentence[1:]
        if (len(temp) > 1):
            if data.get(temp, 0):
                values = data[temp]
                res.extend(get_match(values, count, 0, temp, 1))
    return res



def add_(count, sentence, data):

    res = []
    for i in range(len(sentence) - 1, 0, -1):
        if sentence[i] != " " and count < 5:
            for ot in abc:
                if count < 5:
                    temp = sentence[:i] + ot + sentence[i:]

                    if data.get(temp, 0):
                        values = data[temp]
                        res.extend(get_match(values, count, i, temp, 1))
                else:
                    break
            if count == 5:
                break
        elif count == 5:
            break

    if count < 5:
        for ot in matching_letters[sentence[0]]:
            if ot != sentence[i] and count < 5:
                temp = ot + sentence

                if data.get(temp, 0):
                    values = data[temp]
                    res.extend(get_match(values, count, 0, temp, 1))
            elif count == 5:
                break
    return res

