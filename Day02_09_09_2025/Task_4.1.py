# Récursion des 6 premiers chiffres de PI

def SixFirstPi(n, result) :
    if n == 1 : return
    result = result + 4*(1/n)
    SixFirstPi(n-2, result)
    print(result)

SixFirstPi(11, 0)