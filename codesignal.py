
# ✅ Part 1 – GCA
# Question 1
# 📝 Task:
# Write a function that takes a string s and returns a new string where:

# Every letter is shifted to its right by one in alphabetical order.

# 'z' becomes 'a', 'Z' becomes 'A'

# Any non-letter characters stay the same

#  You are not allowed to use string built-in methods

#  Example:

# Input:  "abc123XYz!"
# Output: "bcd123YZa!"
# Explanation:

# 'a' → 'b', 'b' → 'c', 'c' → 'd'

# '1', '2', '3' stay the same

# 'X' → 'Y', 'Y' → 'Z', 'z' → 'a'

# '!' stays '!'

#  Forbidden:
# No use of built-in methods like .lower(), .upper(), .isalpha(), etc.

# You can use: ord(), chr(), loops, conditions, +=, append(), etc.



def solution(s):
  result = []
  for char in s:
    if 97 <= ord(char) <= 122:
      if char =="a":
        result.append("b")
      elif char == "b":
          result.append("c")
      elif char == "c":
            result.append("d")
      elif char == "z":
            result.append("a")
      else: result.append(chr(ord(char) + 1))     
    elif 65 <= ord(char) <= 90:
       if char == "X":
          result.append(("Y"))
       elif char == "Y" :
             result.append("Z")   
       else:
         result.append(chr(ord(char) + 1)) 
    else:
       result.append(char)   
  return "".join(result)   
print(solution("abc123XYz!"))  # Output: bcd123YZa!

# ===================================

# Question 2 (from part 1-question2.png):
# Task:
# You are given:

# A list of words (all lowercase English letters)

# A complex word written in camelCase

# Write a function that checks if the camelCase word consists of only words from the given list.

#  Example:


# words = ["apple", "pie", "a", "p", "ple"]
# camel = "applePie"

# Output: ✅ True (because "apple" and "pie" are in the list)

# camel = "applePen"
# Output:  False (if "pen" is not in the list)
words = ["apple", "pie", "a", "p", "ple"]
# camel1 = "applePie"
# camel2 = "applePen"
def solution(words, camel):
   subword = []
   current = ""
   for char in camel:
      if 65 <= ord(char) <= 90:
        if current:
           subword.append(current)
           current = chr(ord(char) + 32)
      else:
         current += char
   if current:
        subword.append(current)
   for word in subword:  
       if word not in words:
               return False
   return True
              

print(solution(words, "applePie"))   # ✅ True
print(solution(words, "applePen"))   # ❌ False
         
            
#    ------------------------------------
# 📝 Task:
# You are given a string s containing only letters and digits.
# Write a function that splits the string into words, where each word 
# starts with a capital letter, and returns a list of the lowercase version of each word.

# You may not use any string methods like .split() or .lower().

#  Example:
# Input:  "ApplePie123Cake456"
# Output: ["apple", "pie", "cake"]
# Ignore any numbers. Only collect letter-only words that start with a capital letter
#  and continue with lowercase letters.      
      
def solution(s):
   result = []
   current= ""
   for char in s:
      if 65 <= ord(char) <= 90:
         if current:
           current = chr(ord(char) + 32)
           result.append(current)
      elif 97 <= ord(char) <=122:
         current += char
      else:
          if current:
           result.append(current)
           current = ""
   if current:
    result.append(current)
    return result  
print(solution("ApplePie123Cake456"))  # Output: ["apple", "pie", "cake"]         
               
# =====================

# Given a string input_string, your task is to write a function that transforms 
# all the lowercase letters to uppercase and all the uppercase letters to lowercase. 
# If the character is not a letter, do not transform it.

# The transformation should be done without using any built-in Python methods,
# it is not allowed to use built-in Python functions like lower(), upper(), or similar in your code.

# For example, for the input string "HelLo WoRld 123", the output should be "hELlO wOrLD 123".
def solution(input_string):
    # TODO: implement the function
    result = []
    for char in input_string:
        if 97 <= ord(char) <= 122:     #lowercase
            result.append(chr(ord(char) - 32))     # convert to uppercase
        elif 65 <= ord(char) <= 90:       #uppercase
            result.append(chr(ord(char) + 32))      #convert to lowercase
        else:
            result.append(char)
    return "".join(result)


print(solution("HELLO"))
print(solution("world"))

# ==========================

# Given a string input_string, return a new string in which
# all occurrences of character c1 in the original string replaced by c2.
# You cannot use any built-in string methods or functions in Python, such as replace().

# Here's an example:

# Python
# Copy to clipboard
# print(replace_character("hello, world", "o", "a"))  
# # Output: "hella, warld"
# In this example, all occurrences of o have been replaced by a.

def replace_character(input_string, c1, c2):
    # TODO: Replace all occurrences of character `c1` in `input_string` with `c2`
    result = []
    
    for char in input_string:
      if char == c1:
        result.append(c2)
      else:
        result.append(char)
    return "".join(result)
print(replace_character("hello, world", "o", "a"))  # Output: "hella, warld"

# ===========================
# You are given a string s. Your task is to write a function that returns a string in which 
# every pair of adjacent characters in the original string is swapped. If the string has an odd length,
#  leave the last character as it is.

# It is not allowed to use Python built-in functions like reverse() or join() in this task,
#  you should implement the solution without using them.

# For example, if you are given the string "abcdef", your function should return "badcfe".
#  If the string is "hello", your function should return "ehllo".
def solution(s):
    result = []
    for i in range(0, len(s) - 1, 2):
        result.append(s[i + 1])
        result.append(s[i])

    if len(s) % 2 != 0:
        result.append(s[-1])  # only this line should be under the if

    final = ""                # moved out
    for char in result:       # moved out
        final += char         # moved out

    return final

print(solution("abcdef"))  # ➜ "badcfe"
print(solution("hello"))   # ➜ "ehllo"    

# ===============================

# You are given a string, and your task is to check whether the provided string
#  is a palindrome, without using any built-in string methods. A string is a palindrome
#   if it reads the same forward and backward, ignoring the casing of letters 
#   ('A' and 'a' are considered the same) and ignoring non-letter characters.

# Return a boolean value: True if the string is a palindrome and False if it is not.

# It is not allowed to use Python built-in functions like reverse(), reversed(), or similar in this task.

def solution(s):
   result = []
   char = s[i]
   for i in range (len(s) // 2):
      if 65 <= ord(char) <= 97:
       result.append(chr(ord(char) + 32))
       if result[i] != result[i -1-i]:
        return False
      else:
         return True
      
# ================================
# You are given a string input_string, your task is to write a function that checks if the string is a palindrome.
def solution(input_string):
    cleaned = []
    for char in input_string:
        code = ord(char)
        # Convert uppercase to lowercase
        if 65 <= code <= 90:  # 'A' to 'Z'
            cleaned.append(chr(code + 32))
        elif 97 <= code <= 122:  # 'a' to 'z'
            cleaned.append(char)
        # ignore non-letters

    # Check palindrome manually
    n = len(cleaned)
    for i in range(n // 2):
        if cleaned[i] != cleaned[n - 1 - i]:
            return False
    return True
