def A(s, n):
    if len(s) >= n:
        return True
    return False


def B(s, n):
    result = 0
    for characters in s:
        if (
            not (32 >= ord(characters) >= 0)
            and not (57 >= ord(characters) >= 48)
            and not (90 >= ord(characters) >= 65)
            and not (122 >= ord(characters) >= 97)
        ):
            result += 1

    if result >= n:
        return True
    return False


def C(s, n):
    result = 0
    for characters in s:
        if 57 >= ord(characters) >= 48:
            result += 1
    if result >= n:
        return True
    return False


A("etsyehdyei", 11)
B("%£%µ£/.", 6)
C("dz;dk,z14dz4dz94dzdz8dz98458489", 5)
