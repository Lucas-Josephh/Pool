# La fonction zip() permet de combiner les deux listes. Les deux listes sont inversés donc on inverse la liste last_name pour avoir les noms et prénom au
# même index. La combinaison donne [(' Jackie ', ' Chan '), (' Chuck ', ' Norris '), (' Arnold ', ' Schwarzenegger '), (' Sylvester ', ' Stallone ')]


first_names = [" Jackie ", " Chuck ", " Arnold ", " Sylvester "]
last_names = [" Stallone ", " Schwarzenegger ", " Norris ", " Chan "]
magic = [*zip(first_names, last_names[::-1])]
print(magic)
print()
print(magic[0])
print(magic[3])
print(magic[1][0])
print(magic[0][1])
print(magic[2])
