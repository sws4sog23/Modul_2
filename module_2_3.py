my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
b = -1
while a < len(my_list):
    a += 1
    b += 1
    if my_list[b] == 0:
        continue
    if my_list[b] > 0:
        print(my_list[b])
    else:
        break
