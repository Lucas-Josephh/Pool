import pygame
import pygame_textinput
import hanged_c
import hanged_const
import words


def hanged_game():
    hang = hanged_c.Hanged([], [], "", "", 0)
    hang_const = hanged_const
    hang.set_hide_word(
        words.words().replace("é", "e").replace("à", "a").replace("è", "e").upper()
    )
    hang.set_rm_found_words(hang.get_hide_word())
    proposition = ""

    while (
        (hang.get_penality() <= 12)
        and (len(hang.get_rm_found_words()) != 0)
        and (hang.get_hide_word() != proposition)
    ):
        show_game(
            hang.get_hide_word(),
            hang.get_words_found(),
            hang.get_words_say(),
            hang.get_penality(),
        )
        print("\nProposez une lettre ou un mot")
        proposition = input().upper()
        if hang.isLetter(proposition):
            if hang.isWord(proposition):
                if not (proposition in hang.get_words_say()):
                    if proposition in hang.get_hide_word():
                        hang.set_words_say(proposition)
                        hang.set_words_found(proposition)
                        hang.rm_found_words(proposition)
                        print(hang_const.HANGED_SUCCESS)
                    else:
                        hang.set_words_say(proposition)
                        hang.set_penality(1)
                        print(hang_const.HANGED_WRONG)
                else:
                    print(hang_const.HANGED_ALREADY_SAY)
            else:
                if not hang.isSentenceFound(proposition):
                    hang.set_penality(5)
                    print(hang_const.HANGED_NOT_FOUND_SENTENCE)
        else:
            print(hang_const.HANGED_NOT_LETTER)

    if hang.get_penality() < 12:
        print(hang_const.HANGED_WIN)
        print(f"Tentatives : {len(hang.get_words_found()) + len(hang.get_words_say())}")
        exit()
    print(hang_const.HANGED_LOOSE)


def show_game(hide_word, find_words, say_word, penality):
    print("==========================================")
    for show_word in hide_word:
        if show_word in find_words:
            print(show_word, end=" "),
        else:
            print("_", end=" ")
    print(f"\nLettres dites : {say_word}")
    print(f"Tentatives restantes : {12 - penality}")
    print("==========================================")


def show_screen(hide_word):
    pygame.init()
    WIDTH = 1200
    HEIGH = 800
    screen = pygame.display.set_mode((WIDTH, HEIGH))

    # Initialisation des styles
    pygame.font.init()
    default_font = pygame.font.get_default_font()
    font_renderer_words = pygame.font.Font(default_font, 20)
    font_renderer_strokes = pygame.font.Font(default_font, 30)

    labels = [
        font_renderer_words.render(words, 1, (255, 255, 255)) for words in hide_word
    ]
    words_not_found = [
        font_renderer_strokes.render("_", 1, (255, 255, 255))
        for i in range(len(hide_word))
    ]

    # Dessin du pendu
    # Tête
    pygame.draw.circle(screen, (255, 255, 255), (300, 300), 50)

    # Corps
    pygame.draw.line(screen, (255, 255, 255), (300, 300), (300, 450), 5)

    # Bras
    pygame.draw.line(screen, (255, 255, 255), (300, 395), (380, 395), 5)
    pygame.draw.line(screen, (255, 255, 255), (300, 395), (220, 395), 5)

    # Jambes
    pygame.draw.line(screen, (255, 255, 255), (300, 450), (250, 530), 5)
    pygame.draw.line(screen, (255, 255, 255), (300, 450), (350, 530), 5)

    # Structure en partant de la tête
    pygame.draw.line(screen, (255, 255, 255), (300, 300), (300, 150), 5)

    # Barre latérale haut
    pygame.draw.line(screen, (255, 255, 255), (300, 150), (100, 150), 5)

    # Barre diagonale
    pygame.draw.line(screen, (255, 255, 255), (150, 150), (100, 200), 5)

    # Barre horizontale
    pygame.draw.line(screen, (255, 255, 255), (100, 150), (100, 650), 5)

    # Barre latérale bat
    pygame.draw.line(screen, (255, 255, 255), (100, 650), (0, 650), 5)
    pygame.draw.line(screen, (255, 255, 255), (100, 650), (200, 650), 5)

    # Initialisation de l'input box utilisation de la bibliothèque pygame_textinput créé par l'utilisateur "Nearoo"
    # DOC : https://github.com/Nearoo/pygame-text-input

    # Création de l'objet input
    input_text = pygame_textinput.TextInputVisualizer()
    input_text.font_color = (255, 255, 255)
    clock = pygame.time.Clock()

    # Création du bouton d'envoie
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(400, 650, 100, 30))
    label_button = font_renderer_words.render("Envoyer", 1, (0, 0, 255))

    while True:
        space = 0
        for i in range(len(labels)):
            screen.blit(labels[i], (400 + space + 2, 600))
            screen.blit(words_not_found[i], (400 + space, 600))
            space += 30

        screen.blit(label_button, (410, 655))
        screen.blit(info_text, (400, 500))
        events = pygame.event.get()
        input_text.update(events)
        screen.blit(input_text.surface, (400, 700))

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (400 + 100) >= event.dict["pos"][0] >= 400 and (
                    650 + 30
                ) >= event.dict["pos"][1] >= 650:
                    if active_button:
                        val_input = input_text.value
                        input_text.value = ""
        pygame.display.update()
        clock.tick(30)


hanged_game()
