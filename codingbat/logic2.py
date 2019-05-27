def lucky_sum(a=0, b=0, c=0):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a+b+c


def fix_teen(n=0):
    return 0 if ((n >= 13 and n <= 19) and (n != 16 and n != 15)) else n


def no_teen_sum(a=0, b=0, c=0):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


# print(no_teen_sum(1, 2, 3))
# print(no_teen_sum(2, 13, 1))
# print(no_teen_sum(2, 1, 14))
# print(lucky_sum(1, 2, 13))
# print(lucky_sum(1, 13, 3))
