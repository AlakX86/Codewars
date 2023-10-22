def persistence(n):
    times_counter = 0
    while n >= 10:
        times_counter += 1
        multiplications = 1
        for num in str(n):
            multiplications *= int(num)
        n = multiplications
    return times_counter
