import time
import pygame
import hanged_c
import hanged_const
import words
import stickman
import text


def init_game(hang):
    hang.set_hide_word(
        words.words()
        .replace("é", "e")
        .replace("à", "a")
        .replace("è", "e")
        .replace("ç", "c")
        .replace("â", "a")
        .upper()
    )

    hang.set_rm_found_words(hang.get_hide_word())


def hanged_game(hang, proposition):
    hang_const = hanged_const
    proposition = proposition.upper()

    if hang.get_penality() >= 4:
        return hang_const.HANGED_LOOSE
    if len(hang.get_rm_found_words()) == 1:
        return hang_const.HANGED_WIN

    if hang.isLetter(proposition):
        if hang.isWord(proposition):
            if not (proposition in hang.get_words_say()):
                if proposition in hang.get_hide_word():
                    hang.set_words_say(proposition)
                    hang.set_words_found(proposition)
                    hang.rm_found_words(proposition)
                    return hang_const.HANGED_SUCCESS
                else:
                    hang.set_words_say(proposition)
                    hang.set_penality(1)
                    return hang_const.HANGED_WRONG
            else:
                return hang_const.HANGED_ALREADY_SAY
        else:
            if not hang.isSentenceFound(proposition):
                hang.set_penality(5)
                return hang_const.HANGED_NOT_FOUND_SENTENCE
    else:
        return hang_const.HANGED_NOT_LETTER


def show_screen():
    hang = hanged_c.Hanged()
    pygame.init()
    init_game(hang)

    clock = pygame.time.Clock()
    WIDTH = 1127
    HEIGH = 562
    screen = pygame.display.set_mode((WIDTH, HEIGH))
    background = pygame.image.load(
        "Day09_18_09_2025\\hanged\\src\\background-single.png"
    )
    background.convert()
    screen.blit(background, (0, 0))

    stick = stickman.Stickman(screen, 0, 300)
    stick.pos(350, 500)

    font = pygame.font.SysFont("arial", 48)

    hiding_word = text.Text(screen, "")
    hiding_word.create()

    result = ""
    for i in range(len(hang.get_hide_word())):
        result += " _ "

    hiding_word.modifier(result)
    hiding_word.display(screen, len(result), ((WIDTH // 2) - (WIDTH // 2) // 2, 20))

    info_message = text.Text(screen, "")
    info_message.create()
    info_message.display(screen, len(result), ((WIDTH // 2) - (WIDTH // 2) // 2, 90))

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                info = hanged_game(hang, chr(event.key))

                info_message.modifier(info)
                info_message.display(
                    screen, len(info), ((WIDTH // 2) - (WIDTH // 2) // 2, 90)
                )

                hide_word = ""
                for hide in hang.get_hide_word():
                    if hide in hang.get_words_found():
                        hide_word += f" {hide} "
                    else:
                        hide_word += " _ "
                    hiding_word.modifier(hide_word)
                    hiding_word.display(
                        screen, len(hide_word), ((WIDTH // 2) - (WIDTH // 2) // 2, 20)
                    )
        if hang.get_penality() == 1:
            stick.bottom_bar()
        elif hang.get_penality() == 2:
            stick.vertical_bar()
        elif hang.get_penality() == 3:
            stick.top_sidebar()
        elif hang.get_penality() == 4:
            stick.diagonal_bar()
        elif hang.get_penality() == 5:
            stick.rope()
        pygame.display.flip()
        clock.tick(500)


show_screen()
