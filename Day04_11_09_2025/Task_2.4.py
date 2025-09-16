for i in range(-30, 31):
    if i % 3 == 0:
        print("Fizz", end="")
    if i % 5 == 0:
        print("Buzz", end="")
    if i % 15 != 0:
        print(f"\nL'entier {i} n'est pas divisible par 5 et/ou 3")
