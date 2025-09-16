# Récursion des 6 premiers chiffres de PI

def irrational(var, result) :
    if var < 1 : return
    result = var**2 / (6 + (var+2)**2)
    irrational(var-2, result)
    print(result+3)

irrational(55, 0)