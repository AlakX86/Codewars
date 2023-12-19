def isPP(n):
    for m in range(2, int(n**0.5) + 1):
        k = 2
        while m**k <= n:
            if m**k == n:
                return [m, k]
            k += 1
    return None