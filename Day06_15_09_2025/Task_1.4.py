def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print("O O O O O O")


def ham():
    print(" ============ ")


nbr_sandwiche = int(input())

if nbr_sandwiche > 0:
    for i in range(1, nbr_sandwiche + 1):
        print(f"\nSandwiche {i} : ")
        print(bread())
        print(lettuce())
        print(tomato())
        print(ham())
        print(ham())
        print(bread())
else:
    print("I can't do this!,")
