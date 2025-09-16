number = int(input())

if number == 42 : 
    print('a')
elif number%2 == 0 and number < 21 :
    print('d')
elif number <= 21 : 
    print('b')
elif number%2 == 0 : 
    print('c')
elif number%2 != 0 and number >= 45 :
    print('e')
else :
    print('i')
    