# Entrer clavier string et mettre uniquement la première lettre en majuscule

print("Comment vous appellez-vous ?")
name = input().lower()
print("Bonjour", name.upper()[0] + name[1:])