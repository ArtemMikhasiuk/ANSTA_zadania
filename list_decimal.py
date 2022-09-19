from decimal import Decimal

def list_decimal(num1, num2, step):
    list_d = []
    num1 = Decimal(num1)
    num2 = Decimal(num2)
    step = Decimal(step)

    while num1 <= num2:
        list_d.append(num1)
        num1 += step

    return list_d

