def calcul_pow(n, p):
    result = 1
    for i in range(0, p):
        result *= n
    return result


print(calcul_pow(42, 168))
