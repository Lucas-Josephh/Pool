# Prédiction : ?

# Vérification : Cela donne i

# p[:: -2] : le "-" signifi qu'on prend la liste en partant de la fin.
# Le "2" signifi qu'on récupère un caractères sur deux en commençant par stocker le dernier.
# Exemple : tab = "123456789" => tab[:: -2]
# On se positionne à la fin on garde le 9 et on supprime le 8 puis on garde le 7 et on supprime le 6 ...
# On se retrouve avec "13579" Attention il ne faut pas oublié la signification de "-" qui inverse la chaine
# donc le vrai résultat de tab [:: -2] est 97531

# p [:5] signifi qu'on garde les 5 premiers caractères de la liste
# Exemple : tab = "123456789" => tab[:5]
# Resultat = 12345

# p [:: -1] Même chose que pour p[:: -2] sauf que le -1 signifi qu'on prend 1 caractère sur 1 donc tout les caractères 
# Donc le "1" ne change pas la chaîne cependant le "-" l'inverse donc le "-1" permet simplement d'inverser la chaîne
# Exemple : tab = "123456789" => tab[:: -1]
# Resultat = 987654321

# p [3:] signifi qu'on récupère toute la chaîne sauf les 3 premiers caractères.
# Exemple : tab = "123456789" => tab[3:]
# Resultat = 456789

# Revenons au code. Appliquons explicitement chaque instruction pour trouver i.
# On commence par p [:: -2] donc on prend 1 caractère sur deux en partant de la fin sachant que les espaces sont des caractères
# et on inverse.
# Résultat = igeca (Attention il y a un espace au début)

# Appliquons maintenant p[:5] à notre résultat ( igeca) donc on prend les 5 premiers caractères
# Résultat = igec (Comme l'espace est un caractère, cela supprimer le "a" de la chaîne)

# Appliquon p[:: -1] donc on prend 1 caractère sur 1 en partant de la fin et on inverse.
# Résultat = cegi

# Appliquon p[3:] donc on supprime les 3 premiers caractères de la chaîne et on garde le reste.
# Résultat = i

# Le résultat final est bien "i"

p = " abcdefghij "
print (p [:: -2][:5][:: -1][3:])