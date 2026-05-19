"""
https://leetcode.com/problems/length-of-last-word/description/?envType=problem-list-v2&envId=string
"""

def length_last_word(string: str) -> int:
    words: list[str] = string.strip().split(' ')
    if not words:
        return 0
    return len(words[-1])

sentence = "   fly me   to   the moon  "
print("Input: ", sentence)
print("Output: ", length_last_word(sentence))