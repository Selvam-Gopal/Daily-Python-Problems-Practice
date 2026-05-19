"""
Leetcode Problem Link: https://leetcode.com/problems/roman-to-integer/description/?envType=problem-list-v2&envId=string
"""

def roman_integer(string: str) -> int:
    roman_values: dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
    result: int = 0
    for i in range(len(string)):
        if i+1 < len(string) and roman_values[string[i]] < roman_values[string[i+1]]:
            result -= roman_values[string[i]]
        else:
            result += roman_values[string[i]]
    return result

roman = "MCMXCIV"
print("Input: ", roman)
print("Output: ", roman_integer(roman))