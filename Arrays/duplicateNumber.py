def duplicateNumber():
    nums = list(map(int, input().split()))
    for i in nums:
        m = abs(i)
        if nums[m-1] < 0:
            return m
        else:
            nums[m-1] *= -1


print(duplicateNumber())
