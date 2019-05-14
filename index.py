from algos.challenges_100 import allLongestStrings, evenDigitsOnly, factorializeANumber, reverseAString, isTandemRepeat
from algos.others import splitString
from helpers.helpers import test


test("isTandemRepeat", isTandemRepeat("abc"), False)
test("isTandemRepeat", isTandemRepeat("tandemtandem"), True)
test("reverseAString", reverseAString("abc"), "cba")
test("reverseAString", reverseAString("12345"), "54321")
test("factorializeANumber", factorializeANumber(5), 120)
test("factorializeANumber", factorializeANumber(10), 3628800)
test("evenDigitsOnly", evenDigitsOnly(1234), False)
test("evenDigitsOnly", evenDigitsOnly(1264), False)
test("evenDigitsOnly", evenDigitsOnly(8264), True)
test("splitString", splitString("12??34", "??"), ["12", "34"])
test("allLongestStrings", allLongestStrings(["abcd", "Abc", "de"]), ["abcd"])
