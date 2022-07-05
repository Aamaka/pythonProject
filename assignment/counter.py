from collections import Counter


def list_func(lis):
    lis_count = Counter(lis)
    printing_list = []
    x = lis_count.most_common()
    for i in x:
        printing_list.append(list(i).pop(0))
    return printing_list


list_func(["i am a girl", "i am a girl"])
