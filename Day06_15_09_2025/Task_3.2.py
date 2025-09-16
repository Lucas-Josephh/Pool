import Task_3_1


def passcheck(fun, nbr_char, password):
    return fun(password, nbr_char)


print(passcheck(Task_3_1.A, 16, "kdjfmpdlepdc7./?ja"))
print(passcheck(Task_3_1.B, 3, "kdjfmpdlepd4.%/ja"))
print(passcheck(Task_3_1.C, 1, "kdjfmpdlepd4./%ja"))
