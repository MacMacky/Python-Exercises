def sum13(nums=[]):
    total = 0
    lenNums = len(nums)
    if lenNums == 0:
        return 0
    else:
        i = 0
        while i < lenNums:
            if nums[i] != 13:
                total += nums[i]
                i += 1
            else:
                i += 2
        return total


def has22(nums=[]):
    lengtho = len(nums)
    if lengtho == 0:
        return False
    else:
        for i in range(lengtho):
            if nums[i:i+2] == [2, 2]:
                return True
        return False


def count_evens(nums=[]):
    return len([num for num in nums if num % 2 == 0])
#print(centered_average([-10, -4, -2, -4, -2, 0]))
