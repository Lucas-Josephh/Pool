# doubler chaque lettre du string de la sortie clavier

sentence = input()

for i in range(0, len(sentence)) :
    print(sentence[i] + sentence[i], end='')

