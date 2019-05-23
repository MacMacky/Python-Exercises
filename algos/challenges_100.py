
def all_longest_strings(arr=[]):
    lenArr = len(arr)
    if lenArr == 0:
        return arr
    else:
        lenStrs = [len(item) for item in arr]
    return [item for item in arr if len(item) == max(lenStrs)]


def even_digits_only(n=1):
    digits = list(str(n))
    for digit in digits:
        if int(digit) % 2 == 1:
            return False
    return True


def factorialize_a_number(num=1):
    if num == 1:
        return 1
    else:
        return num * factorialize_a_number(num-1)


def reverse_a_string(string=""):
    listo = list(string)
    listo.reverse()
    reversedStr = ""
    for char in listo:
        reversedStr += char
    return reversedStr


def reverse_a_string2(string=""):
    return string[::-1]


def reverse_a_string3(string=""):
    return "".join(reversed(string))


def is_tandem_repeat(string=""):
    half = len(string)//2
    return string[0:half] == string[half:len(string)]


def allLongestStrings(arr=[]):
    maxLen = max([len(string) for string in arr])
    return [string for string in arr if len(string) == maxLen]


def array_replace(arr=[], elementToReplace=0, substitutionElement=0):
    if len(arr) == 0 or arr == None:
        return []
    return [(substitutionElement if el == elementToReplace else el) for el in arr]


def largest_of_four(arrays=[[]]):
    return [max(arr) for arr in arrays]


def confirm_ending(string="", target=""):
    return True if string.find(target) >= 0 else False


def largest_number(n=1):
    return 9 if n == 1 else int("9" * n)


def proper_noun_correction(noun=""):
    return noun if noun.istitle() else (noun[0].upper() + noun[1:].lower())


def domain_types(domains=[]):
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


def add_two_digits(num=0):
    if type(num) is not int:
        return 0
    else:
        return sum([int(char) for char in list(str(num))])


def add_numbers(*args):
    return sum(args)


def check_palindrome(string=""):
    return reverse_a_string2(string) == string


def find_max(arr=[]):
    return max(arr)


def chunk_monkey(arr=[], size=1):
    if len(arr) == 0 or size is None:
        return 0
    else:
        chunk_arr = []
        for i in range(0, len(arr), size):
            chunk_arr.append([item for item in arr[i:i+size]])
        return chunk_arr


def is_prime(num=0):
    if num == 0 or num == 1 or num is None:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        half = num // 2
        for i in range(2, half+1):
            if (num % i) == 0:
                return False
        return True


def sum_all_primes(num=0):
    if num == 0 or num == 1 or num is None:
        return 0
    else:
        return sum([x for x in range(0, num+1) if is_prime(x)])
