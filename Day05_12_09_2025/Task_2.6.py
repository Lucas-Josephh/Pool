# Le résultat de ce code est [21, 6, 2, 9, 6, 5] on va détailler comment on obtient ce résultat.
# for x in [42, 3, 4, 18, 3, 10]      =>   x prend la valeur de chaque élément de la liste
# if x % 2 == 0   =>   On vérifi d'abord si x est un multiple de 2
# x // 2          =>   Si la condition est vrai alors on fait une division entière
# else x * 2      =>   Si la condition est fausse alors on multipli par 2 et devient multiple de 2

print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])
