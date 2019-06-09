def factorial(n=1):
    return 1 if ((n == 0) or (n == 1)) else n * factorial(n-1)


def is_palindrome(string=""):
    length = len(string)
    if length == 0:
        return True
    else:
        if string[0] == string[length-1]:
            return is_palindrome(string[1:length-1])
        else:
            return False


def power(base=1, exponent=1):
    return base if exponent == 1 else base * power(base, exponent-1)


def product_of_array(arr=[]):
    return arr[0] if len(arr) == 1 else arr[0] * product_of_array(arr[1:])


def flatten_array(arr=[[]]):
    lengtho = len(arr)
    flatten_arr = []
    for item in arr:
        if type(item) == list:
            flatten_arr.extend(flatten_array(item))
        else:
            flatten_arr.append(item)
    return flatten_arr


def bunny_ears(bunnies):
    return 0 if bunnies == 0 else 2 + bunny_ears(bunnies-1)


def count_7(num=0):
    lengtho = len(str(num))
    if lengtho == 1:
        return 1 if num == 7 else 0
    else:
        remainder = num % 10
        return 1 + count_7(num//10) if remainder == 7 else count_7(num//10)


def count_abc(string=""):
    if len(string) == 0:
        return 0
    else:
        sub = string[0:3]
        return 1 + count_abc(string[1:]) if sub == 'abc' or sub == 'aba' else count_abc(string[1:])
