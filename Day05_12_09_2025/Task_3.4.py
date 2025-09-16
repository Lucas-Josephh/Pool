dictionnary = {
    " dalmatians ": 101,
    "pi": 3.14,
    " beast ": 3 * 2 * 111,
    " life ": 42,
    " googol ": 10 ^ 100,
}

my_list = []
for dict in dictionnary:
    my_list.append(dict)

print(dictionnary[min(my_list)])
