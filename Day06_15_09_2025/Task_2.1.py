def sum_integer(n):
    if n == 0:
        return 0
    return sum_integer(n - 1) + n


print(sum_integer(8))
