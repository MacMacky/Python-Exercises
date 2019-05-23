from algos.challenges_100 import domain_types, is_prime, chunk_monkey, largest_number, proper_noun_correction, confirm_ending, all_longest_strings, largest_of_four, array_replace, even_digits_only, factorialize_a_number, reverse_a_string, is_tandem_repeat, reverse_a_string2, reverse_a_string3, add_two_digits, add_numbers, check_palindrome, find_max
from algos.others import splitString
from helpers.helpers import test, describe


test("is_prime", is_prime(5), True)
test("is_prime", is_prime(2), True)
test("is_prime", is_prime(0), False)
test("is_prime", is_prime(1), False)
test("is_prime", is_prime(), False)
test("chunk_monkey", chunk_monkey([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
test("chunk_monkey", chunk_monkey([1, 2, 3, 4], 3), [[1, 2, 3], [4]])
test("find_max", find_max([1, 2, 3]), 3)
test("find_max", find_max([0, 5, 4, 1, 2]), 5)
test("check_palindrome", check_palindrome("racecar"), True)
test("check_palindrome", check_palindrome("abac"), False)
test("check_palindrome", check_palindrome("aba"), True)
test("add_numbers", add_numbers(6), 6)
test("add_numbers", add_numbers(1, 2, 3), 6)
test("add_numbers", add_numbers(6), 6)
test("add_numbers", add_numbers(1, 2, 3), 6)
test("add_two_digits", add_two_digits("11"), 0)
test("add_two_digits", add_two_digits(53), 8)
test("domain_types", domain_types(["sure.org", "yj.con", "amawa.con"]), [
     "organization", "not recognized", "not recognized"])
test("domain_types", domain_types(["aamawa.ss.com"]), ["company"])
test("proper_noun_correction", proper_noun_correction("mark"), "Mark")
test("proper_noun_correction", proper_noun_correction("John"), "John")
test("largest_number", largest_number(1), 9)
test("largest_number", largest_number(2), 99)
test("confirmEnding", confirm_ending("Abstration", "action"), False)
test("confirmEnding", confirm_ending("Abstraction", "action"), True)
test("largest_of_four", largest_of_four(
    [[1, 2, 3, 4], [5, 4, 3, 2], [5, 4, 3, 2], [5, 4, 3, 2]]), [4, 5, 5, 5])
test("largest_of_four", largest_of_four(
    [[1, 2, 3, 4], [5, 4, 3, 2], [10, 11, 15, 20], [1, 2, 3, 4]]), [4, 5, 20, 4])
test("array_replace", array_replace([], 5, 5), [])
test("array_replace", array_replace([5, 4, 3, 2, 1], 5, 4), [4, 4, 3, 2, 1])
test("all_longest_strings", all_longest_strings(
    ["aaabbb", "", "c"]), ["aaabbb"])
test("all_longest_strings", all_longest_strings(
    ["aaa", "bbb"]), ["aaa", "bbb"])
test("reverse_a_string3", reverse_a_string3("abc"), "cba")
test("reverse_a_string3", reverse_a_string3("abcd"), "dcba")
test("reverse_a_string2", reverse_a_string2("abc"), "cba")
test("reverse_a_string2", reverse_a_string2("abcd"), "dcba")
test("reverse_a_string", reverse_a_string("abc"), "cba")
test("is_tandem_repeat", is_tandem_repeat("abc"), False)
test("is_tandem_repeat", is_tandem_repeat("tandemtandem"), True)
test("reverse_a_string", reverse_a_string("abc"), "cba")
test("reverse_a_string", reverse_a_string("12345"), "54321")
test("factorialize_a_number", factorialize_a_number(5), 120)
test("factorialize_a_number", factorialize_a_number(10), 3628800)
test("even_digits_only", even_digits_only(1234), False)
test("even_digits_only", even_digits_only(1264), False)
test("even_digits_only", even_digits_only(8264), True)
test("splitString", splitString("12??34", "??"), ["12", "34"])
test("all_longest_strings", all_longest_strings(
    ["abcd", "Abc", "de"]), ["abcd"])
