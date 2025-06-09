def even_numbers(n):
    evens = []
    for num in range(1, n + 1):
        if num % 2 == 0:
            evens.append(num)
        else:
            pass
    return evens