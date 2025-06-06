#  Question Type 3: Counting or Logic
# Like:

# "Given a string or array, count specific elements based on conditions."
# Sample:
# Task: Count how many times each digit (0–9) appears in a string

#the correct code:
def solution(s):
    count = [0] * 10  # Initialize a list to count digits 0-9
    result = []  # Initialize an empty list to store the result
    for char in s:
        if '0' <= char <= '9':  # Check if the character is a digit
            count[ord(char) - ord('0')] += 1  # Increment the count for that digit
    for i in range(10):
         result.append([str(i), count[i]])# Return the counts as a list of lists
    return result
# can say like this too. so then no need to have result variable:
    # return [[str(i), count[i]] for i in range(10)]

print(solution("66a12321a155746999"))  # Output: [['0', 0], ['1', 3], ['2', 2], ['3', 1], ...]

# # ===================================
# # Question 3 (from part 1-question3.png):
# # Given an array a, return an array b where:
# # b[i] = a[i] * 2 if a[i] is even, otherwise b[i] = a[i] + 1

# # Example input:
# # a = [2, 3, 4, 5]
# # Expected output:
# # b = [4, 4, 8, 6]

def solution (a):
    result = []
    for char in a:
        if char %2 == 0:
           result.append([ord(char) * 2]) 
        else:
            char % 2 != 0
            result.append([ord(char) + 1])
    return result
print(solution([2, 3, 4, 5]))  # Output: [4, 4, 8, 6]

# ========================================

# You are given a string, and your task is to check whether the provided string is
#  a palindrome, without using any built-in string methods. A string is a palindrome
#   if it reads the same forward and backward, ignoring the casing of letters ('A' and 'a' are considered the same)
#    and ignoring non-letter characters.

# Return a boolean value: True if the string is a palindrome and False if it is not.

# It is not allowed to use Python built-in functions like reverse(), reversed(), or similar in this task.


def solution(input_string):
    result = []
    for char in input_string:
        code = ord(char)
        # Convert uppercase to lowercase
        if 65 <= code <= 90:  # 'A' to 'Z'
            result.append(chr(code + 32))
        elif 97 <= code <= 122:  # 'a' to 'z'
            result.append(char)
        # ignore non-letters

    # Check palindrome manually
    n = len(result)
    for i in range(n // 2):
        if result[i] != result[n - 1 - i]:
            return False
    return True

print(solution("RaceCar!"))  # True
print(solution("hello"))     # False
print(solution("A man, a plan, a canal, Panama"))  # True

