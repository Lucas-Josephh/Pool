import random
from english_words import get_english_words_set

web2lowerset = get_english_words_set(["web2"], lower=True)

index = 0
nbr = random.randint(0, len(web2lowerset) - 1)

for word in web2lowerset:
    if index == nbr:
        print(word)
        exit
    index += 1
