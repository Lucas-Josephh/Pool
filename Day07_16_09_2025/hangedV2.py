from asyncio import sleep
import random
import time
import words

# Cette version du pendu ajoute un nombre de joueur (bot) définit par le joueur principal (5 bots maximum) avec une option permettant
# de choisir si les propostions de lettre et de mots seront cachés de tous ou non. Pour qu'il y ai une possibilité qu'aucun joueur ne
# gagnent, chaque mot ou lettre proposés seront propre à chaque joueur cependant tout le monde joue sur le même pendu.
# Le nombre de tentative est divisé par le nombre de joueur présent dans la partie.
# Si un joueur n'a plus de tentative, il sera alors éliminé et la partie continuera jusqu'a ce que le mot soit trouvé ou que tous
# les joueurs soient éliminés.


Joueurs = {
    "Player": {"penality": 0, "say_words": []},
    "Bot1": {"penality": 0, "say_words": []},
    "Bot2": {"penality": 0, "say_words": []},
    "Bot3": {"penality": 0, "say_words": []},
    "Bot4": {"penality": 0, "say_words": []},
    "Bot5": {"penality": 0, "say_words": []},
}


def hanged():
    hide_word = (
        words.words().replace("é", "e").replace("à", "a").replace("è", "e").upper()
    )

    find_words = []
    proposition = ""
    find_all_words = False
    player_currently = ""
    list_player = ["Player"]

    print("Choisissez un nombre de joueur entre 0 et 5")
    nbr_player = input()
    if not nbr_player.isdigit():
        print("Partie arrêté ! ")
        print("Veuillez définir un nombre de joueur entre 0 et 5")
        return

    nbr_player = int(nbr_player)
    if nbr_player != 0:
        for i in range(1, nbr_player + 1):
            list_player.append(f"Bot{i}")

        player_currently = f"Bot{nbr_player}"
    else:
        player_currently = "Player"

    show_game(
        hide_word, find_words, [], Joueurs[player_currently]["penality"], nbr_player
    )

    while (len(list_player) > 0 and find_all_words == False) and (
        proposition != hide_word
    ):
        eliminated = ""
        if nbr_player == 0:
            if Joueurs[player_currently]["penality"] > 12:
                eliminated = player_currently
        else:
            if Joueurs[player_currently]["penality"] > 12 // nbr_player:
                eliminated = player_currently

        if (list_player.index(player_currently) + 1) <= len(list_player) - 1:
            player_currently = list_player[list_player.index(player_currently) + 1]
        else:
            player_currently = list_player[0]

        if eliminated != "":
            list_player.remove(eliminated)
            print("\n========================/!\\===========================\n")
            print(f"                         Le joueur {eliminated} est éliminé !")
            print("\n========================/!\\===========================\n")

        print(f"\nC'est au tour de {player_currently} de proposer une lettre ou un mot")
        if player_currently == "Player":
            proposition = input().upper()
        else:
            proposition = chr(random.randint(65, 90))

        if control_proposition(proposition):
            if len(proposition) == 1:
                if (proposition in hide_word) and not (
                    proposition in Joueurs[player_currently]
                ):
                    find_words.append(proposition)
                    Joueurs[player_currently]["say_words"].append(proposition)
                    print(
                        f"\nBravo au joueur {player_currently} qui à trouvé une lettre !"
                    )
                elif proposition in Joueurs[player_currently]["say_words"]:
                    print(
                        f"\nJoueur {player_currently}, vous avez déjà proposé cette lettre"
                    )
                else:
                    Joueurs[player_currently]["penality"] += 1
                    Joueurs[player_currently]["say_words"].append(proposition)
                    print(f"\nLe joueur {player_currently} s'est trompé !\\")
            else:
                if proposition != hide_word:
                    Joueurs[player_currently]["penality"] += 5 // nbr_player
                    print(
                        f"\nLe mot proposé par le joueur {player_currently} n'est pas le bon !"
                    )

        else:
            print(
                f"\nJoueur {player_currently}, veuillez mettre que des lettres dans votre proposition"
            )

        if show_game(
            hide_word,
            find_words,
            Joueurs[player_currently]["say_words"],
            Joueurs[player_currently]["penality"],
            nbr_player,
        ):
            find_all_words = True
        if nbr_player != 0:
            time.sleep(3)
    print("\nLa partie est terminé !")

    if len(list_player) == 0:
        print("Aucun des joueurs n'a réussi à trouver le mot caché")
        print(f"Le mot était {hide_word}\n")

    elif Joueurs[player_currently]["penality"] < 12:
        print(
            f"Le joueur {player_currently} à réussi à trouver le mot caché qui était {hide_word} !"
        )
        print(
            f"Tentatives : {len(find_words) + len(Joueurs[player_currently]["say_words"])}"
        )


def control_proposition(proposition):
    for characters in proposition:
        if not (90 >= ord(characters) >= 65):
            return False
    return True


def show_game(hide_word, find_words, say_word, penality, nbr_player):
    print(
        "===================================================================================="
    )
    find_all_words = True
    for show_word in hide_word:
        if show_word in find_words:
            print(show_word, end=" "),
        else:
            print("_", end=" ")
            find_all_words = False
    print(f"\nWords say : {say_word}")
    if nbr_player == 0:
        print(f"Tentatives restantes : {12 - penality}")
    else:
        print(f"Tentatives restantes : {(12//nbr_player) - penality}")
    print(
        "===================================================================================="
    )
    return find_all_words


hanged()
