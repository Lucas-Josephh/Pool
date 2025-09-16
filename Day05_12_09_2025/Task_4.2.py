my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 1, 2, 7, 4, 8, 6, 5, 9, 9]

for list in my_list:
    if my_list.count(list) != 1:
        my_list.remove(list)

# ============== / optionnel \ ==============
my_list.sort()
# ===========================================

print(my_list)
