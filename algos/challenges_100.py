
def allLongestStrings(arr=[]):
    lenArr = len(arr)
    if lenArr == 0:
        return arr
    else:
        lenStrs = [len(item) for item in arr]
    return [item for item in arr if len(item) == max(lenStrs)]


def evenDigitsOnly(n=1):
    digits = list(str(n))
    for digit in digits:
        if int(digit) % 2 == 1:
            return False
    return True


def factorializeANumber(num=1):
    if num == 1:
        return 1
    else:
        return num * factorializeANumber(num-1)


def reverseAString(string=""):
    listo = list(string)
    listo.reverse()
    reversedStr = ""
    for char in listo:
        reversedStr += char
    return reversedStr


def isTandemRepeat(string=""):
    half = len(string)//2
    return string[0:half] == string[half:len(string)]
