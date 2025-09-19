import pygame
import hanged_c
import hanged_const
import words
import asyncio
import stickman
import text


async def hanged_game(hang):
    clock = pygame.time.Clock()
    hang_const = hanged_const
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
    proposition = ""

    print("La fonction asyncrone fonctionne parfaitement !")

    while (
        (hang.get_penality() <= 12)
        and (len(hang.get_rm_found_words()) != 0)
        and (hang.get_hide_word() != proposition)
    ):

        print("\nProposez une lettre ou un mot")
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


async def show_game(hide_word, find_words, say_word, penality):
    print("==========================================")
    for show_word in hide_word:
        if show_word in find_words:
            print(show_word, end=" "),
        else:
            print("_", end=" ")
    print(f"\nLettres dites : {say_word}")
    print(f"Tentatives restantes : {12 - penality}")
    print("==========================================")


async def show_screen(hang):
    pygame.init()
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
    stick.bottom_bar()
    stick.vertical_bar()
    stick.top_sidebar()
    stick.diagonal_bar()
    stick.rope()

    font = pygame.font.SysFont("arial", 48)

    hiding_word = text.Text(
        font, "", (0, 255, 0), ((WIDTH // 2) - (WIDTH // 2) // 2, 0)
    )
    hiding_word.creer()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                hang.set_choose_key(chr(event.key).upper())

        hide_word = ""
        for hide in hang.get_hide_word():
            if hide in hang.get_words_found():
                hide_word += hide
            else:
                hide_word += " _ "
        hiding_word.modifier(hide_word)

        hiding_word.draw(screen)
        pygame.display.flip()
        clock.tick(30)


async def main():
    hang = hanged_c.Hanged([], [], "", "", "ok", 0)

    await asyncio.gather(hanged_game(hang), show_screen(hang))


if __name__ == "__main__":
    asyncio.run(main())
