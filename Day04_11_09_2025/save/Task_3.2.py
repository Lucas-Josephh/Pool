print("Entrer votre message")
message = input().replace(" ", "")

print("\nEntrer la clé de chiffrement")
key = int(input().replace(" ", ""))

result = ""


def LowerUperChar(mess, itIsUpper):
    encryptedMessage = ""
    minimum = 97  # Lettre "a" dans le tableau ASCII
    maximum = 123  # Lettre après "z" dans le tableau ASCII
    # upLow permet de savoir si la lettre que l'on traite est une majuscule ou minuscule
    if itIsUpper:
        minimum = 65  # Lettre "A" dans le tableau ASCII
        maximum = 91  # Lettre après "Z" dans le tableau ASCII

    # La fonction ord() permet de convertir le caractère "mess" en entier ASCII pour les minuscules de a -> z les valeurs sont entre 97 -> 122
    # la var "maximum" permet de savoir si on est au dela de "z" dont sa valeur entier ASCII est 122. Même chose pour les majuscule
    if ord(mess) - key < minimum:

        # chr() permet de convertir un entier en caractère ASCII. le résultat du calcule est convertit en en caractère.
        # Détail du calcul : prenons la lettre "b" et la clé "4"
        # L'entier de "b" est 98 on doit donc décaler la lettre de 4 vers la gauche or on va en dessous de "a" qui à une valeur de 96 donc :
        #
        # -key - (ord(mess) - minimum) + maximum
        # -4 - (98 - 97) + 123
        # -4 - 1 + 123
        # -5 + 123
        # 118
        # On supprimer 1 à notre clé car entre a et b il y a 1 décalage. Ensuite on part de la lettre juste après "z" et on enlève 5 ce qui nous donne "v"
        # Donc le résultat de "b" key : 4 est "v"
        encryptedMessage += chr(abs((key - (ord(mess) - minimum)) - maximum))

    else:

        # Dans le cas ou on ne descend pas en dessous de la lettre "a", on décale simplement la lettre en convertissant la lettre en entier ASCII avec ord() puis en ajoutant la clé
        # et on reconverti le résultat en caractère avec chr()
        encryptedMessage += chr(ord(mess) - key)
    return encryptedMessage


for mess in message:
    result += LowerUperChar(mess, mess.isupper())

print(result)
