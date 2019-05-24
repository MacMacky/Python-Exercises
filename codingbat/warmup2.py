
def test(testName, returnValue, expectedValue):
    try:
        assert returnValue == expectedValue
        print("Test " + testName + " Success.")
    except AssertionError as e:
        print("Test " + testName + " Failed.")


def string_bits(string=""):
    return string[0::2]


def string_match(a="", b=""):
    lenA = len(a)
    lenB = len(b)
    if lenA != lenB:
        return 0
    else:
        count = 0
        for i in range(lenA):
            if len(a[i:i+2]) == 2 and a[i:i+2] == b[i:i+2]:
                count += 1
        return count


def last2(string=""):
    lenS = len(string)
    if lenS == 0:
        return 0
    else:
        counto = 0
        pattern = string[lenS-2:lenS]
        for i in range(lenS-2):
            if string[i:i+2] == pattern:
                counto += 1
        return counto


def front_times(string="", n=0):
    return string[0:3] * n if type(string) == str else ""


def array123(nums=[]):
    lengtho = len(nums)
    if lengtho == 0:
        return False
    else:
        pattern = [1, 2, 3]
        for i in range(lengtho):
            if nums[i:i+3] == pattern:
                return True
        return False


def array_front9(nums=[]):
    lengtho = len(nums)
    if lengtho == 0:
        return False
    else:
        return True if 9 in nums[0:4] else False


def array_count9(nums=[]):
    return len([num for num in nums if num == 9])


def string_times(string="", n=0):
    return string * n if type(string) == str else ""


def string_splosion(string=""):
    lengtho = len(string)
    if lengtho == 0:
        return ""
    else:
        new_string = ""
        for i in range(lengtho + 1):
            new_string += string[0:i]
        return new_string


test('string_splosion', string_splosion("Code"), 'CCoCodCode')
test('string_splosion', string_splosion("abc"), 'aababc')
test('string_splosion', string_splosion("ab"), 'aab')
# test('string_times', string_times('Hi', 2), 'HiHi')
# test('string_times', string_times('Hi', 3), 'HiHiHi')
# test('string_times', string_times('Hi', 1), 'Hi')
# test('array_count9', array_count9([1, 2, 9]), 1)
# test('array_count9', array_count9([1, 9, 9]), 2)
# test('array_count9', array_count9([1, 9, 9, 3, 9]), 3)
# test('array_front9', array_front9([1, 2, 9, 3, 4]), True)
# test('array_front9', array_front9([1, 2, 3, 4, 9]), False)
# test('array_front9', array_front9([1, 2, 3, 4, 4]), False)
# test('array123', array123([1, 1, 2, 3, 1]), True)
# test('array123', array123([1, 1, 2, 4, 1]), False)
# test('array123', array123([1, 1, 2, 1, 2, 3]), True)
# test('front_times', front_times('Chocolate', 2), 'ChoCho')
# test('front_times', front_times('Chocolate', 3), 'ChoChoCho')
# test('front_times', front_times('Abc', 3), 'AbcAbcAbc')
# test('last2', last2('hixxhi'), 1)
# test('last2', last2('xaxxaxaxx'), 1)
# test('last2', last2('axxxaaxx'), 2)
# test('string_match', string_match('abc', 'abc'), 2)
# test('string_bits', string_bits('Hello'), 'Hlo')
# test('string_bits', string_bits('Heeololeo'), 'Hello')
