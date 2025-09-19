#!/usr/bin/python3


class Hanged:

    def __init__(
        self,
        words_say=[],
        words_found=[],
        hide_word="",
        del_found_words="",
        message="",
        penality=0,
        letter="",
    ):
        self.words_say = words_say
        self.words_found = words_found
        self.hide_word = hide_word
        self.del_found_words = del_found_words
        self.message = message
        self.penality = penality
        self.letter = letter

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

    def get_rm_found_words(self):
        return self.del_found_words

    def set_rm_found_words(self, sentence):
        print(sentence)
        self.del_found_words = sentence

    def set_choose_key(self, _letter):
        self.letter = _letter

    def get_choose_key(self):
        return self.letter

    def set_message(self, msg):
        self.message = msg

    def get_message(self):
        return self.message

    def rm_found_words(self, word):
        self.del_found_words = self.del_found_words.replace(word, "")

    def isLetter(self, word):
        for characters in word:
            if not (90 >= ord(characters) >= 65):
                return False
        return True

    def isWord(self, word):
        return len(word) == 1

    def isSentenceFound(self, sentence):
        return sentence == self.get_hide_word
