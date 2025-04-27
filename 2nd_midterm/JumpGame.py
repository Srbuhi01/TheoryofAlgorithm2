def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps

nums1 = [2, 3, 1, 1, 4]
print(jump(nums1))


nums2 = [2, 3, 0, 1, 4]
print(jump(nums2))
