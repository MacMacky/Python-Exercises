def alarm_clock(day=0, vacation=False):
    if vacation and (day == 0 or day == 6):
        return "off"
    else:
        if not vacation:
            if (day != 0) and (day != 6):
                return '7:00'
            else:
                return '10:00'


#
