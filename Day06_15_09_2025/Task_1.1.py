# Prédiction : Le premier print va afficher 42. Le deuxième print va afficher 52


def f1():
    return 42


def f2(x):
    return 2 * x


print(f1())
print(f2(5) + f1())
