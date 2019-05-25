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


print(sum13([1, 2, 3, 4, 13, 5]))
