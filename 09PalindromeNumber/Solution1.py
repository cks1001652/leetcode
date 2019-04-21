class Solution:
    # Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    # Example 1:

    # Input: 121
    # Output: true
    # Example 2:

    # Input: -121
    # Output: false
    # Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    # Example 3:

    # Input: 10
    # Output: false
    # Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    # Follow up:

    # Coud you solve it without converting the integer to a string?

    # idea: reverse the whole strings
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            if x % 10 ==0:
                return False
            else:
                if str(x)[::-1] == str(x):
                    return True
            return False
