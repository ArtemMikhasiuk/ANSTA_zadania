def brak(list_a, number):
    list_brak = []
    list_a = sorted(list_a)

    list_b = []
    for i in range(1, (number + 1), 1):
        list_b.append(i)

    while len(list_b) != 0:

        if list_a.count(list_b[0]) == 0:
            list_brak.append(list_b[0])
            list_b.remove(list_b[0])
            continue

        else:
            list_b.remove(list_b[0])
            continue

    return list_brak

