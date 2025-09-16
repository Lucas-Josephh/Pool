print("Entrer votre message")
message = input().replace(" ", "").lower()

print("\nEntrer la clé de chiffrement")
key = input().replace(" ", "")

result = ""


def crypted(mess, key):
    # La fonction ord() permet de convertir le caractère key en son entier de la table ASCII
    # On vérifi que l'écart dans l'alphabet entre ma key et a + la position de mon caractère ne dépassent pas la lettre z
    if ord(mess) + (ord(key) - ord("a")) > ord("z"):

        # Pour comprendre ce calcule, il faut commencer par la partie de gauche : abs((ord("z") - ord(mess) - (ord(key) - ord("a"))))
        # on va décortiquer :
        # (ord(key) - ord("a")) => On veut connaitre le nombre de lettre qui séparent ma key à la première lettre de l'alphabet soit "a" ce qui me donne le nombre
        # de décalage à faire vers la droite en partant de mon caractère.
        # (ord("z") - ord(mess) => Ensuite on veut savoir l'écart qu'il y a entre mon caractère et la dernière lettre de l'alphabet soit "z" ce qui me donne le nombre
        # que je dois soustraire à ma key.
        # ((ord("z") - ord(mess)) - ((ord(key) - ord("a"))) => on soustrait le tout et on obtient le nombre de décalage à faire en partant de "a" le nombre
        # obtenu est toujours négatif donc on met la fonction abs() pour la rendre positif
        # ord("a") - 1) => Ensuite on se positionne sur le caractère juste avant le "a"
        # Pour finir j'ajoute mon décalage pour arriver sur ma lettre

        # Cas concret :
        # Mon caractère est "x"
        # Ma key est "e"
        # La valeur ASCII de "x" est 120
        # La valeur ASCII de "e" est 101
        # La valeur ASCII de "a" est 97
        # La valeur ASCII de "z" est 122
        #
        # (ord(key) - ord("a")) => (101 - 97) = 4 => le nombre de décalage à faire vers la droite pour trouver la valeur finale (sur la partie "mon caractère").
        # (ord("z") - ord(mess) => (122 - 120) = 2 => le nombre de lettre qui sépare "x" et "z" avec "z" inclut (sur la partie clé).
        # (ord("z") - ord(mess) - (ord(key) - ord("a")) => (122 - 120 - (101 - 97)) = 2 - 4 = -2 => on a soustrait le nombre de décalage entre "x" et "z" à notre nombre
        # de décalage initiale soit "4" et avec la valeur absolue on obtient "2" donc on a déjà effectué un décalage de "2" il en reste encore deux à faire en partant de
        # la valeur juste avant "a".
        # La deuxième partie du calcul est simple on se positionne sur le caractère juste avant "a" puis on effectu un décalage de "2" vers la droite.
        # (97 - 1) + 2
        # 98
        # Le résultat final du calcule est 98 avec pour valeur char ASCII "b".
        # On peut vérifier le résultat dans une table de Vigenère https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re
        return chr((ord("a") - 1) + abs((ord("z") - ord(mess) - (ord(key) - ord("a")))))
    else:

        # Dans le cas ou on ne dépasse pas "z", on vérifi l'écart entre ma key et a puis on ajoute cet écart à la position de mon caractère
        return chr(ord(mess) + (ord(key) - ord("a")))


# Permet d'égaliser les longueurs entre message et key
if len(message) != len(key):
    while len(message) != len(key):
        if len(message) > len(key):
            for i in range(0, len(key)):
                key += key[i]
        else:
            key = key[: len(message)]

for i in range(0, len(message)):
    result += crypted(
        message[i],
        key[i],
    )

print(result)
