def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print("O O O O O O")


def ham():
    print(" ============ ")


def vegetable():
    print(" ------------- ")


def makeSandwiche(vegan):
    nbr_sandwiche = int(input())

    if nbr_sandwiche > 0:
        if not vegan:
            for i in range(1, nbr_sandwiche + 1):
                print(f"\nSandwiche {i} : ")
                print(bread())
                print(lettuce())
                print(tomato())
                print(ham())
                print(ham())
                print(bread())
        else:
            for i in range(1, nbr_sandwiche + 1):
                print(f"\nSandwiche {i} : ")
                print(bread())
                print(lettuce())
                print(tomato())
                print(vegetable())
                print(vegetable())
                print(bread())
    else:
        print("I can't do this!,")


makeSandwiche(True)
