def inversions(nums):
    counter = 0
    for i in range(len(nums)):
        for k in range(len(nums)):
            if i < k and nums[i] > nums[k]:
                counter += 1
    return counter
