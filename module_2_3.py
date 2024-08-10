my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    a += 1
    if my_list[a-1] == 0:
        continue
    if my_list[a-1] > 0:
        print(my_list[a-1])
    else:
        break
