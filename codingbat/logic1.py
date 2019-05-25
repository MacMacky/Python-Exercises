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


print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))
