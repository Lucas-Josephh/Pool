number = int(input())

for i in range(2, int(number / 2) + 1):
    for b in range(2, number):
        if (number - (b - 1)) % i == 0:
            print(number - (b - 1), end=" ")
    print()
