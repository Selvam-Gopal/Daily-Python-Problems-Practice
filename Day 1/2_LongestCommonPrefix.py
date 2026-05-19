"""
https://leetcode.com/problems/longest-common-prefix/description/?envType=problem-list-v2&envId=string
"""

def longest_common_prefix(strings: list[str]) -> str:
    result: str = ""
    prefix: str = strings[0]
    for i in range(len(prefix)):
        for j in strings:
            if i == len(j) or prefix[i] != j[i]:
                return result
        result += prefix[i]
    return result

words = ["flower","flow","flight","fan"]
print("Input: ",words)
print("Output: ",longest_common_prefix(words))