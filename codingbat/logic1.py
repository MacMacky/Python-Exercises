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


print(cigar_party(30, False))
print(cigar_party(50, True))
print(cigar_party(70, True))
