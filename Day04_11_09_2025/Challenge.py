number = int(input())
chaine = input()

if number == 0:
    exit

elif (
    "a" in chaine
    or "e" in chaine
    or "i" in chaine
    or "o" in chaine
    or "u" in chaine
    or "y" in chaine
):
    print(number)

else:
    print(chaine)
