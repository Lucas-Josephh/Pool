chaine = (
    input()
    .lower()
    .replace(" ", "")
    .replace("!", "")
    .replace(".", "")
    .replace("?", "")
    .replace(";", "")
    .replace(",", "")
    .replace("/", "")
    .replace(":", "")
)


def palindrome(long):
    if long == -1:
        return ""

    return chaine[long] + palindrome(long - 1)


if palindrome(len(chaine) - 1) == chaine:
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")
