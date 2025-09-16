import words


def hanged():
    say_word = []
    find_words = []
    hide_word = (
        words.words().replace("é", "e").replace("à", "a").replace("è", "e").upper()
    )
    penality = 0
    proposition = ""
    find_all_words = False
    show_game(hide_word, find_words, say_word, penality)
    while (penality < 12) and (find_all_words == False) and (proposition != hide_word):
        print("\nProposez une lettre ou un mot")
        proposition = input().upper()
        if control_proposition(proposition):
            if len(proposition) == 1:
                if (proposition in hide_word) and not (proposition in say_word):
                    find_words.append(proposition)
                    say_word.append(proposition)
                    print("\nBravo ! vous avez trouvé une lettre :)")
                elif proposition in say_word:
                    print("\nVous avez déjà dis cette lettre :x")
                else:
                    penality += 1
                    say_word.append(proposition)
                    print("\nNon ! cette lettre n'est pas dans le mot :\\")
            else:
                if proposition != hide_word:
                    penality += 5
                    print("\nLe mot proposé n'est pas le bon !")

        else:
            print("\nVeuillez mettre que des lettres dans votre proposition")

        if show_game(hide_word, find_words, say_word, penality):
            find_all_words = True

    if penality < 12:
        print("\nVous avez réussi à trouver le mot !")
        print(f"Tentatives : {len(find_words) + len(say_word)}")
    else:
        print("Vous avez perdu :( Vous n'echapperez pas à la pendaison !)")


def control_proposition(proposition):
    for characters in proposition:
        if not (90 >= ord(characters) >= 65):
            return False
    return True


def show_game(hide_word, find_words, say_word, penality):
    print("==========================================")
    find_all_words = True
    for show_word in hide_word:
        if show_word in find_words:
            print(show_word, end=" "),
        else:
            print("_", end=" ")
            find_all_words = False
    print(f"\nWords say : {say_word}")
    print(f"Tentatives restantes : {12 - penality}")
    print("==========================================")
    return find_all_words


hanged()
