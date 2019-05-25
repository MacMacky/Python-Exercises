def alarm_clock(day=0, vacation=False):
    if vacation and (day == 0 or day == 6):
        return "off"
    else:
        if not vacation:
            if (day != 0) and (day != 6):
                return '7:00'
            else:
                return '10:00'


def caught_speeding(speed=0, is_birthday=False):
    if is_birthday or (speed <= 60):
        return 0
    elif (speed >= 61) and (speed <= 80):
        return 1
    else:
        return 2


def cigar_party(cigars=0, is_weekend=False):
    if is_weekend or ((cigars >= 60) and (cigars <= 60)):
        return True
    else:
        return False


def date_fashion(you=0, date=0):
    if (you >= 8) or (date >= 8):
        return 2
    elif (you <= 2) or (date <= 2):
        return 0
    else:
        return 1


def in1to10(n=0, outside_mode=False):
    if ((n >= 1) and (n <= 10)):
        return True
    elif ((n < 1) or (n >= 11)) and outside_mode:
        return True
    else:
        return False


def love6(a=0, b=0):
    if (a == 6) or (b == 6) or (abs(a+b) == 6) or (abs(a-b) == 6):
        return True
    else:
        return False


print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))
