
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


def reverseAString2(string=""):
    return string[::-1]


def reverseAString3(string=""):
    return "".join(reversed(string))


def isTandemRepeat(string=""):
    half = len(string)//2
    return string[0:half] == string[half:len(string)]


def allLongestStrings(arr=[]):
    maxLen = max([len(string) for string in arr])
    return [string for string in arr if len(string) == maxLen]


def arrayReplace(arr=[], elementToReplace=0, substitutionElement=0):
    if len(arr) == 0 or arr == None:
        return []
    return [(substitutionElement if el == elementToReplace else el) for el in arr]


def largestOfFour(arrays=[[]]):
    return [max(arr) for arr in arrays]


def confirmEnding(string="", target=""):
    return True if string.find(target) >= 0 else False


def largestNumber(n=1):
    return 9 if n == 1 else int("9" * n)


def properNounCorrection(noun=""):
    return noun if noun.istitle() else (noun[0].upper() + noun[1:].lower())


def domainTypes(domains=[]):
    length = len(domains)
    if length == 0 or domains is None:
        return []
    else:
        result = []
        table = {
            "info": "information",
            "org": "organization",
            "com": "company",
            "net": "network"
        }
        for domain in domains:
            arr = domain.split('.')
            try:
                result.append(table[arr[len(arr)-1]])
            except KeyError as e:
                result.append("not recognized")
                continue
        return result


def addTwoDigits(num=0):
    if type(num) is not int:
        return 0
    else:
        return sum([int(char) for char in list(str(num))])


def addNumbers(*args):
    return sum(args)


def checkPalindrome(string=""):
    return reverseAString2(string) == string


def findMax(arr=[]):
    return max(arr)
