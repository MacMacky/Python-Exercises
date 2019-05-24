from re import findall


def count_hi(string):
    return len([i for i in range(len(string)) if string[i:i+2] == 'hi'])


def end_other(a="", b=""):
    lenA = len(a)
    lenB = len(b)
    return True if a[lenA-3:lenA].lower() == b[lenB-3:lenB].lower() else False


def double_char(string=""):
    lens = len(string)
    if lens == 0:
        return ""
    else:
        return "".join([char * 2 for char in string])


def cat_dog(string=""):
    lens = len(string)
    if lens == 0:
        return ""
    else:
        countDogs = 0
        countCats = 0
        for i in range(lens):
            if string[i:i+3] == 'cat':
                countCats += 1
            elif string[i:i+3] == 'dog':
                countDogs += 1
        return countCats == countDogs


def count_code(string=""):
    lens = len(string)
    if lens == 0:
        return ""
    else:
        counto = 0
        for i in range(lens):
            if len(findall(r'co\De', string[i:i+4])) >= 1:
                counto += 1
        return counto


def xyz_there(string=""):
    lens = len(string)
    if lens == 0:
        return ""
    else:
        result = findall(r'.?xyz', string)
        return True if len(result) >= 1 and len(result[0]) == 3 else False


print(xyz_there('xyzabc'))
