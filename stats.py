def num_of_words(text):
    lst = text.split(" ")

    return len(lst)


def convert_to_dict(text):
    lst = text.split(" ")

    dct = {}

    for word in lst:
        for character in word:
            if character.lower() in dct:    #Note that we want it lowered in the if statement
                dct[character.lower()] += 1
            else:
                dct[character.lower()] = 1

    return dct


def sort_dict(dct):
    lst = []

    for key in dct:
        lst.append({"character": key, "num": dct[key]})
    
    lst.sort(reverse=True, key=lambda x: x["num"]) # i used lambda :D
    return lst


def sort_on(dict):
    return dict["num"]