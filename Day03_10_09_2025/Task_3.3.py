# Faire la somme des deux nombre

print("Choississez deux nombre")
numbers = input()
splitNumbers = numbers.split(" ")
if len(splitNumbers) == 2 and isinstance(int(splitNumbers[0]), (int)) and isinstance(int(splitNumbers[1]), (int)) :
    print(sum([int(splitNumbers[0]), int(splitNumbers[1])]))
else :
    print("Veuillez choisir deux nombres")
