import random
import time

start = time.time()

my_list = []

for i in range(0, 1000000):
    my_list.append(random.randint(0, 5))

my_list.sort()
print(my_list)

print(time.time() - start)
