"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=string
"""

def first_occurrence(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.find(needle)
    else:
        return -1

haystack = "override"
needle = "ride"
print(f"Input: Haystack = {haystack}, Needle = {needle}")
print("Output: ", first_occurrence(haystack, needle))