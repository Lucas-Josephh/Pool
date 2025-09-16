# Faire la somme des chiffres d'un nombre

def sumDigit(n) :
    result = 0
    for i in range(0,len(str(n))) :
        result = result + int(str(n)[i])
    print("Somme des chiffre : ", result)

sumDigit(123434565)