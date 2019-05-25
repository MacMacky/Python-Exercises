def first_last6(nums=[]):
    if len(nums) == 0:
        return False
    else:
        return True if nums[0:1][0] == 6 or nums[len(nums)-1:len(nums)][0] == 6 else False


def same_first_last(nums=[]):
    lenN = len(nums)
    if lenN == 0:
        return False
    else:
        return True if nums[0:1] == nums[lenN-1:lenN] else False


def make_pi():
    return [3, 1, 4]


def common_end(a=[], b=[]):
    lenA = len(a)
    lenB = len(b)
    if lenA == 0 or lenB == 0:
        return False
    else:
        return True if (a[0] == b[0] or (a[lenA-1] == b[lenB-1])) else False


def sum3(nums):
    return sum(nums)


def reverse3(nums=[]):
    return nums[::-1]


def max_end3(nums=[]):
    return [max(nums) for i in range(3)]


def sum2(nums=[]):
    return sum(nums[0:2])
