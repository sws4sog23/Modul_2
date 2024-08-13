n = int(input('Введите число с первого камня '))
result = []
for i in range(1, n):
    k = 1
    for j in range(i + 1, n + 1 - k):
        s = i + j
        if n % s == 0:
            result.append(i)
            result.append(j)
        k += 1

result = ''.join(map(str, result))
print(result)
