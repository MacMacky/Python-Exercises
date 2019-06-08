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
