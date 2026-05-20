"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

def remove_duplicate(nums: list[int]) -> list:
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return nums[:i+1]

arr = [0,0,1,1,1,2,2,3,3,4]
print("Input: ", arr)
print("Output: ", remove_duplicate(arr))