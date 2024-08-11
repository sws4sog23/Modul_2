numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    elif i == 2:
        primes.append(i)
        continue
    for j in range(2, i):
        is_prime = bool(i % j)
        if is_prime is True and j < i - 1:
            continue
        elif is_prime is False:
            not_primes.append(i)
            break
        else:
            primes.append(i)
print(primes)
print(not_primes)
