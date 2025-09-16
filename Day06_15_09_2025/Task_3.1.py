def A(s, n):
    if len(s) >= n:
        print(f"{s} contain {n} characters")
        return
    print(f"{s} doesn't contain {n} characters")


def B(s, n):
    result = 0
    for characters in s:
        if (
            characters == "!"
            or ","
            or ";"
            or "?"
            or "."
            or "@"
            or "/"
            or "\\"
            or ":"
            or "*"
            or "%"
        ):
            result += 1

    if result >= n:
        print(f"{s} contain exactely {n} characters")
    else:
        print(f"{s} doesn't contain exactely {n} characters")


def C(s, n):
    result = 0
    for characters in s:
        if 57 >= ord(characters) >= 48:
            result += 1
    if result >= n:
        print("Il y a le bon nombre de chiffre")
    else:
        print("il n'y a pas assez de chiffre")


print(A("etsyehdyei", 11))
print(B("%£%µ£/.", 6))
print(C("dz;dk,z14dz4dz94dzdz8dz98458489", 5))
