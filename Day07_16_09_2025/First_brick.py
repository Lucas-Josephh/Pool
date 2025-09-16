def interger_comparaison(n):
    if n >= 12:
        print("You loose !")
    else:
        print("You win !")


choose_integer = input()
if choose_integer.isdigit():
    interger_comparaison(int(choose_integer))
else:
    print("Veuillez choisir un nombre entier")
