"""
https://leetcode.com/problems/two-sum/submissions/2007737729/
"""

def two_sum(nums: list[int], target: int) -> list:
    num_map: dict = {}
    # output: list[list[int]] = []  To show all possible pairs
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]
            # output.append([num_map[complement], i])
        num_map[nums[i]] = i
    return []

arr: list[int] = [8,9,10,4,6,2,3,1,21,0]
total: int = 9
print(f"Input: List = {arr}, Target = {total}")
print("Output: ", two_sum(arr, total))