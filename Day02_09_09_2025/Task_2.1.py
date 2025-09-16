# Additionner la suite 1 + 11 + 111 + ... + 111111111

def suite9() :
   var=1
   result=0
   for i in range(0,9) :
      result = result + var
      var = var * 10 + 1
      print(result)

suite9()

# ==========================================================================================

# Additionner la suite de 1 + 11 + 111 + ... + 111111111
# Mettre le résultat de la suite à la puissance 2, 3, 4, 5

def suite9Puissance() :
    var=1
    result=0
    for i in range(0,9) :
       result = result + var
       var = var * 10 + 1
    print("Résultat de l'addition de la suite : ", result)
    print()
    for i in range(2,6) :
       print("Résultat puissance de ", i, " : ", result**i)

suite9Puissance()

# ==========================================================================================

# Additionner la suite de 1 + 11 + 111 + ... + 111111111 + 1111111111
# Mettre le résultat de la suite à la puissance 2, 3, 4, 5

def suite10Puissance() :
    var=1
    result=0
    for i in range(0,10) :
       result = result + var
       var = var * 10 + 1
    print("Résultat de l'addition de la suite : ", result)
    print()
    for i in range(2,6) :
       print("Résultat puissance de ", i, " : ", result**i)

suite10Puissance()
# ==========================================================================================

# Additionner la suite de 1 + 11 + 111 + ... + 111111111 + 1111111111 + 11111111111
# Mettre le résultat de la suite à la puissance 2, 3, 4, 5

def suite11Puissance() :
    var=1
    result=0
    for i in range(0,10) :
       result = result + var
       var = var * 10 + 1
    print("Résultat de l'addition de la suite : ", result)
    print()
    for i in range(2,6) :
       print("Résultat puissance de ", i, " : ", result**i)

suite11Puissance()

# ==========================================================================================