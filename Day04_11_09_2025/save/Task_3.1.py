print("Entrer votre message")
message = input().replace(" ", "")

print("\nEntrer la clé de chiffrement")
key = int(input().replace(" ", ""))

result = ""


def LowerUperChar(mess, itIsUpper):
    encryptedMessage = ""
    minimum = 96  # Lettre juste avant "a" dans le tableau ASCII
    maximum = 122  # Lettre "z" dans le tableau ASCII
    # upLow permet de savoir si la lettre que l'on traite est une majuscule ou minuscule
    if itIsUpper:
        minimum = 64  # Lettre juste avant "A" dans le tableau ASCII
        maximum = 90  # Lettre "Z" dans le tableau ASCII

    # La fonction ord() permet de convertir le caractère "mess" en entier ASCII pour les minuscules de a -> z les valeurs sont entre 97 -> 122
    # la var "maximum" permet de savoir si on est au dela de "z" dont sa valeur entier ASCII est 122. Même chose pour les majuscule
    if ord(mess) + key > maximum:

        # chr() permet de convertir un entier en caractère ASCII. le résultat du calcule est convertit en en caractère.
        # Détail du calcul : prenons la lettre" x" et la clé "4"
        # L'entier de "x" est 120 on doit donc décaler la lettre de 4 or on dépasse "z" qui à une valeur de 122 donc :
        #
        # key - (maximum - ord(mess)) + minimum
        # 4 - (122 - 120) + 96
        # 4 - 2 + 96
        # 2 + 96
        # 98
        # On supprimer 2 à notre clé car entre x et z il y a 2 décalage. Ensuite on part de la lettre juste avant "a" et on ajoute 2 ce qui nous donne "b"
        # Donc le résultat de "x" key : 4 est "b"
        encryptedMessage += chr((key - (maximum - ord(mess))) + minimum)

    else:

        # Dans le cas ou on ne dépasse pas la lettre "z", on décale simplement la lettre en convertissant la lettre en entier ASCII avec ord() puis en ajoutant la clé
        # et on reconverti le résultat en caractère avec chr()
        encryptedMessage += chr(ord(mess) + key)
    return encryptedMessage


for mess in message:
    result += LowerUperChar(mess, mess.isupper())

print(result)
