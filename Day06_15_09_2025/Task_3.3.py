import Task_3_1


def passcheck(fun, nbr_char, password):
    return fun(password, nbr_char)


print("Veuillez définir un mot de passe")
mdp = input()

if not (passcheck(Task_3_1.A, 16, mdp)):
    print("Votre mot de passe n'est pas assez long")
elif not (passcheck(Task_3_1.B, 3, mdp)):
    print("Vous devez mettre au moins 3 caractères spéciaux")
elif not (passcheck(Task_3_1.C, 1, mdp)):
    print("Vous devez mettre au moins un chiffre")
else:
    print("Votre mot de passe à été enregistré avec succès !")
