def passcheck(nbr_char, password):
    special_char = 0
    digit_char = 0
    if len(password) >= nbr_char:
        for characters in password:
            if (
                not (32 >= ord(characters) >= 0)
                and not (57 >= ord(characters) >= 48)
                and not (90 >= ord(characters) >= 65)
                and not (122 >= ord(characters) >= 97)
            ):
                special_char += 1
            else:
                if 57 >= ord(characters) >= 48:
                    digit_char += 1

        if special_char >= 3 and digit_char >= 1:
            print("Votre mot de passe respecte les critères !")
            return
    print("Votre mot de passe ne respecte pas les critères !")


passcheck(16, "kdjfmpdlepdc7./?ja")
passcheck(3, "kdjfmpdlepd4.%/ja")
passcheck(1, "kdjfmpdlepd4./%ja")
