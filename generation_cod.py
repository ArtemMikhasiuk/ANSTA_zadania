def generation_cod(cod1, cod2):
    all_cods = []

    cod1_number = int(cod1[:2] + cod1[3:]) + 1
    cod2_number = int(cod2[:2] + cod2[3:])

    for i in range(cod1_number, cod2_number, 1):
        i = str(i)
        all_cods.append(i[:2] + '-' + i[2:])

    return all_cods
