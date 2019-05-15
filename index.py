from algos.challenges_100 import domainTypes, largestNumber, properNounCorrection, confirmEnding, allLongestStrings, largestOfFour, arrayReplace, evenDigitsOnly, factorializeANumber, reverseAString, isTandemRepeat, reverseAString2, reverseAString3
from algos.others import splitString
from helpers.helpers import test, describe

test("domainTypes", domainTypes(["sure.org", "yj.con", "amawa.con"]), [
     "organization", "not recognized", "not recognized"])
test("domainTypes", domainTypes(["aamawa.ss.com"]), ["company"])
test("properNounCorrection", properNounCorrection("mark"), "Mark")
test("properNounCorrection", properNounCorrection("John"), "John")
test("largestNumber", largestNumber(1), 9)
test("largestNumber", largestNumber(2), 99)
test("confirmEnding", confirmEnding("Abstration", "action"), False)
test("confirmEnding", confirmEnding("Abstraction", "action"), True)
test("largestOfFour", largestOfFour(
    [[1, 2, 3, 4], [5, 4, 3, 2], [5, 4, 3, 2], [5, 4, 3, 2]]), [4, 5, 5, 5])
test("largestOfFour", largestOfFour(
    [[1, 2, 3, 4], [5, 4, 3, 2], [10, 11, 15, 20], [1, 2, 3, 4]]), [4, 5, 20, 4])
test("arrayReplace", arrayReplace([], 5, 5), [])
test("arrayReplace", arrayReplace([5, 4, 3, 2, 1], 5, 4), [4, 4, 3, 2, 1])
test("allLongestStrings", allLongestStrings(["aaabbb", "", "c"]), ["aaabbb"])
test("allLongestStrings", allLongestStrings(["aaa", "bbb"]), ["aaa", "bbb"])
test("reverseAString3", reverseAString3("abc"), "cba")
test("reverseAString3", reverseAString3("abcd"), "dcba")
test("reverseAString2", reverseAString2("abc"), "cba")
test("reverseAString2", reverseAString2("abcd"), "dcba")
test("reverseAString", reverseAString("abc"), "cba")
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
