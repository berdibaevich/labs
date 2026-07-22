
# Reverse Integer (Medium)
# https://leetcode.com/problems/reverse-integer/description/

"""
Example 1:

    Input: x = 123
    Output: 321

Example 2:

    Input: x = -123
    Output: -321

Example 3:

    Input: x = 120
    Output: 21
"""

def reverse(number: int) -> int:
    is_negative = False
    if number < 0:
        number = -number
        is_negative = True

    result = 0
    while number != 0:
        q = number % 10
        result = result * 10 + q
        number //= 10

    if is_negative:
        result = -result

    if result < -2**31 or result > 2**31 - 1:
        return 0

    return result