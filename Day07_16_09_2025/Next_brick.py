import random


def interger_comparaison(my_list):
    return list(my_list)[random.randint(0, len(my_list) - 1)]


print(interger_comparaison({1, 2, 3, 4, 5, 6}))
