# Check if a string is a palindrome without using built-in string methods like lower() or reversed().

# You are given a string, and your task is to check whether the provided string
#  is a palindrome, without using any built-in string methods. A string is a palindrome
#   if it reads the same forward and backward, ignoring the casing of letters 
#   ('A' and 'a' are considered the same) and ignoring non-letter characters.

# Return a boolean value: True if the string is a palindrome and False if it is not.

# It is not allowed to use Python built-in functions like reverse(), reversed(), or similar in this task.


def solution(s):
    result = []  # cleaned characters

    for char in s:
        code = ord(char)
        if 65 <= code <= 90:  # uppercase
            result.append(chr(code + 32))
        elif 97 <= code <= 122:  # lowercase
            result.append(char)

    # Check palindrome
    n = len(result)
    for i in range(n // 2):
        if result[i] != result[n - 1 - i]:
            return False
    return True
