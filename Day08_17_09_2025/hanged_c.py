#!/usr/bin/python3


class Hanged:

    def __init__(
        self,
        words_say,
        words_found,
        hide_word,
        penality,
    ):
        self.words_say = words_say
        self.words_found = words_found
        self.hide_word = hide_word
        self.penality = penality

    def set_words_say(self, word):
        self.words_say.append(word)

    def get_words_say(self):
        return self.words_say

    def set_words_found(self, word):
        self.words_found.append(word)

    def get_words_found(self):
        return self.words_found

    def set_penality(self, penality):
        self.penality += penality

    def get_penality(self):
        return self.penality

    def set_hide_word(self, word):
        self.hide_word = word

    def get_hide_word(self):
        return self.hide_word

    def isLetter(self, word):
        for characters in word:
            if not (90 >= ord(characters) >= 65):
                return False
        return True

    def isWord(self, word):
        return len(word) == 1

    def isSentenceFound(self, sentence):
        return sentence == self.get_hide_word
