# Check if a string is a palindrome without using built-in string methods like lower() or reversed().

# You are given a string, and your task is to check whether the provided string
#  is a palindrome, without using any built-in string methods. A string is a palindrome
#   if it reads the same forward and backward, ignoring the casing of letters 
#   ('A' and 'a' are considered the same) and ignoring non-letter characters.

# Return a boolean value: True if the string is a palindrome and False if it is not.

# It is not allowed to use Python built-in functions like reverse(), reversed(), or similar in this task.


# def solution(s):
#     result = []  # cleaned list

#     for char in s:
#         code = ord(char)
#         if 65 <= code <= 90:  # A-Z
#             result.append(chr(code + 32))  # convert to lowercase
#         elif 97 <= code <= 122:  # a-z
#             result.append(char)  # already lowercase
#         # else: ignore non-letters

#     # Check if reversed matches
#     n = len(result)
#     for i in range(n // 2):
#         if result[i] != result[n - 1 - i]:
#             return False
#     return True



def solution (s):
    result=[]
    for char in s:
        if 65<=ord(char)<=90:
            result.append(chr(ord(char)+ 32))
        elif 97<=ord(char)<=122:
            result.append(char)
    for i in range (len(result)//2):
         if result[i]!= result[len(result)-1-i]:
              return False
    return True
        
# Example usage:
print(solution("Racecar"))  # True
print(solution("Hello"))    # False
