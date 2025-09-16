print("Entrer une phrase")
splitChaine = input().split(" ")
result = ""
for i in range(0, len(splitChaine)):
    result += splitChaine[i][0]
print(result)

# Entre la phrase : Play your trumpet happily on nights
