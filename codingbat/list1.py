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


print(same_first_last([1, 2, 4]))
