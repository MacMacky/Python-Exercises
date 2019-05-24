
def test(testName, returnValue, expectedValue):
    try:
        assert returnValue == expectedValue
        print("Test " + testName + " Success.")
    except AssertionError as e:
        print("Test " + testName + " Failed.")


def diff21(n=0):
    res = abs(n-21)
    return res * 2 if n > 21 else res


def front_back(string=''):
    length = len(string)
    if length == 1:
        return string
    elif length == 2:
        return string[1] + string[0]
    else:
        return string[-1] + string[1:length-1] + string[0]


def front3(string=''):
    return string[0:3] * 3 if type(string) == str else ""


def makes10(a, b):
    return True if ((a == 10) or (b == 10) or abs(a+b) == 10) else False


def missing_char(string="", index=0):
    if type(string) != str:
        return ""
    else:
        if index == 0:
            return string[1:]
        elif index == 1:
            return string[0:1] + string[index+1]
        else:
            return string[0:index] + string[index+1:]


def sum_double(a=0, b=0):
    return (a+b) * 2 if a == b else a+b


def sleep_in(weekday, vacation):
    return True if (not weekday or vacation) else False


def pos_neg(a=0, b=0, negative=False):
    return True if (negative and (a < 0 and b < 0)) else True if ((a > 0 and b < 0) or (a < 0 and b > 0)) else False


def parrot_trouble(talking=False, hour=0):
    return True if (talking and (hour < 7 or hour > 20)) else False


def not_string(string=""):
    return 'not ' + string if string[0:3] != 'not' else string


def monkey_trouble(a_smile=False, b_smile=False):
    return True if a_smile == b_smile else False


test('monkey_trouble', monkey_trouble(True, True), True)
test('monkey_trouble', monkey_trouble(False, False), True)
test('monkey_trouble', monkey_trouble(True, False), False)
test('not_string', not_string('candy'), 'not candy')
test('not_string', not_string('x'), 'not x')
test('not_string', not_string('not bad'), 'not bad')
test('parrot_trouble', parrot_trouble(True, 6), True)
test('parrot_trouble', parrot_trouble(True, 7), False)
test('parrot_trouble', parrot_trouble(False, 6), False)
test('pos_neg', pos_neg(-4, -5, True), True)
test('pos_neg', pos_neg(-1, 1, False), True)
test('pos_neg', pos_neg(1, -1, False), True)
# test('sleep_in', sleep_in(False, False), True)
# test('sleep_in', sleep_in(True, False), False)
# test('sleep_in', sleep_in(False, True), True)
# test('sum_double', sum_double(2, 2), 8)
# test('sum_double', sum_double(3, 2), 5)
# test('sum_double', sum_double(1, 2), 3)
# test('missing_char', missing_char("kitten", 2), 'kiten')
# test('missing_char', missing_char("kitten", 0), 'itten')
# test('missing_char', missing_char("kitten", 3), 'kiten')
# test('makes10', makes10(9, 10), True)
# test('makes10', makes10(9, 9), False)
# test('makes10', makes10(1, 9), True)
# test('front3', front3("a"), "aaa")
# test('front3', front3(1), "")
# test('front3', front3("Chocolate"), "ChoChoCho")
# test('front_back', front_back("ab"), "ba")
# test('front_back', front_back("code"), "eodc")
# test('front_back', front_back("a"), "a")
# test("diff21", diff21(19), 2)
# test("diff21", diff21(10), 11)
# test("diff21", diff21(21), 0)
# test("diff21", diff21(22), 2)
