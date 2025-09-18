import pygame
import hanged_c
import hanged_const
import words
import asyncio
import stickman


async def hanged_game(hang):
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

        await asyncio.gather(
            show_game(
                hang.get_hide_word(),
                hang.get_words_found(),
                hang.get_words_say(),
                hang.get_penality(),
            )
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


async def show_screen(hang):

    pygame.init()
    WIDTH = 1412
    HEIGH = 560
    screen = pygame.display.set_mode((WIDTH, HEIGH))

    # Initialisation des styles
    pygame.font.init()
    default_font = pygame.font.get_default_font()
    font_renderer_words = pygame.font.Font(default_font, 20)
    font_renderer_strokes = pygame.font.Font(default_font, 30)

    labels = [
        font_renderer_words.render(words, 1, (255, 255, 255))
        for words in hang.get_hide_word()
    ]
    words_not_found = [
        font_renderer_strokes.render("_", 1, (255, 255, 255))
        for i in range(len(hang.get_hide_word()))
    ]

    stick = stickman.Stickman(screen)
    stick.rope()
    stick.top_sidebar()
    stick.vertical_bar()
    stick.diagonal_bar()
    stick.bottom_bar()
    stick.head()
    stick.body()
    stick.left_harm()
    stick.right_harm()
    stick.left_leg()
    stick.right_leg()

    clock = pygame.time.Clock()

    while True:
        space = 0
        for i in range(len(labels)):
            screen.blit(labels[i], (400 + space + 2, 600))
            screen.blit(words_not_found[i], (400 + space, 600))
            space += 30

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (400 + 100) >= event.dict["pos"][0] >= 400 and (
                    650 + 30
                ) >= event.dict["pos"][1] >= 650:
                    pass
        pygame.display.update()
        clock.tick(30)


async def main():
    hang = hanged_c.Hanged([], [], "", "", "ok", 0)

    await asyncio.gather(hanged_game(hang), show_screen(hang))


if __name__ == "__main__":
    asyncio.run(main())
