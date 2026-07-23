
# Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

"""
Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def isPalindrome(number: int) -> bool:
    if number < 0:
        return False
    
    original = number
    result = 0

    while number != 0:
        qaldiq = number % 10
        result = result * 10 + qaldiq
        number //= 10

    return original == result



