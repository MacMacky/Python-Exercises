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


def round10(num=0):
    remainder = num % 10
    if remainder < 5:
        return num - remainder
    else:
        return (num-remainder) + 10


def round_sum(a=0, b=0, c=0):
    return round10(a) + round10(b) + round10(c)


def lone_sum(a=0, b=0, c=0):
    return 0 if (a == b == c) else a if (b == c) else b if (a == c) else c if (a==b) else a+b+c
