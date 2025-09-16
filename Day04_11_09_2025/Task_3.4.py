print("Entrer votre message")
message = input().replace(" ", "").lower()

print("\nEntrer la clé de chiffrement")
key = input().replace(" ", "")

result = ""


def decrypted(mess, key):
    if ord(mess) - (ord(key) - ord("a")) < ord("a"):
        return chr(
            abs(((ord(key) - ord("a")) - (ord(mess) - ord("a"))) - (ord("z") + 1))
        )
    return chr(ord(mess) - (ord(key) - ord("a")))


# Permet d'égaliser les longueurs entre message et key
if len(message) != len(key):
    while len(message) != len(key):
        if len(message) > len(key):
            for i in range(0, len(key)):
                key += key[i]
        else:
            key = key[: len(message)]


for i in range(0, len(message)):
    result += decrypted(message[i], key[i])

print(result)
