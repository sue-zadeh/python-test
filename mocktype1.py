# Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

# Given an array of integers numbers, your task is to check all the triples of its consecutive
#  elements for being a zigzag. More formally, your task is to construct an array of length numbers.
# length - 2, where the ith element of the output array equals 1 if the triple (numbers[i], numbers[i + 1],
#  numbers[i + 2]) is a zigzag, and 0 otherwise.

# Example

# For numbers = [1, 2, 1, 3, 4], the output should be solution(numbers) = [1, 1, 0].

# (numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1;
# (numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3;
# (numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4;
# For numbers = [1, 2, 3, 4], the output should be solution(numbers) = [0, 0];

# Since all the elements of numbers are increasing, there are no zigzags.

# For numbers = [1000000000, 1000000000, 1000000000], the output should be solution(numbers) = [0].

# Since all the elements of numbers are the same, there are no zigzags.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.integer numbers

# An array of integers.

# Guaranteed constraints:
# 3 ≤ numbers.length ≤ 100,
# 1 ≤ numbers[i] ≤ 109.

# [output] array.integer

# Return an array, where the ith element equals 1 if the triple (numbers[i], numbers[i + 1],
# 79 numbers[i + 2]) is a zigzag, and 0 otherwise.

# [Python 3] Syntax Tips

# # Prints help message to the console
# # Returns a string
# def helloWorld(name):
#     print("This prints to the console when you Run Tests")
#     return "Hello, " + name
def solution(numbers):
  result = []
  for i in range(len(numbers) -2):
    a, b, c = numbers[i], numbers[i+1], numbers[i+2]
    if (a < b > c) or (a > b < c):
      result.append(1)
    else:
      result.append(0)
  return result
    
#   Given a list of words (all lowercase), and a single complex word written in camelCase,
#   check if the camelCase word can be split into valid words from the list.

# 📤 Output:
# The output would usually be boolean (True or False) or an array of matched words depending on the task.
# In this example:
# Input:
# words = ["apple", "banana", "orange"]
# camelCase = "appleBanana"
# Output:

# True  # because "appleBanana" → "apple", "Banana" → both in list
      
# Function to check if a camelCase word can be split into known words
def can_split_camel_case(words, camelCase):
    result = []   # list to store each extracted word
    word = ""     # temporary word being built

    # Loop through each character in the camelCase string
    for char in camelCase:
        # If the char is uppercase, it's the start of a new word
        if 'A' <= char <= 'Z':
            # Save the current word if it's not empty
            if word:
                result.append(word)
            # Start a new word with lowercase version of uppercase char
            word = chr(ord(char) + 32)
        else:
            # Add the lowercase char to current word
            word += char

    # After the loop, add the last word if it exists
    if word:
        result.append(word)

    # Now check if all split words are in the list
    for part in result:
        if part not in words:
            return False  # at least one part is not in list

    return True  # all parts matched

example_words = ["apple", "banana", "orange"]
print(can_split_camel_case(example_words, "appleBanana"))  # Output: True
print(can_split_camel_case(example_words, "appleOrange"))  # Output: False


# ================================
# Task: sumDivisibleByK
# You're given:
# an array a of integers
# a number k
# Your goal:
# 👉 Count the number of unique index pairs i < j where
#   (a[i] + a[j]) % k == 0

def solution(a,k): 
   count = 0
   for i in range(len(a)):
      for j in range(i+1, len(a)): # always j > i--unique index pairs i < j
        if a[i] + a[j] % k == 0:
           count += 1
   return count  # Return the first pair found
a = [1, 2, 3, 4, 5, 6,7,8,9,10]	
k = 3
print(solution(a, k))  # Output: 4 ✅
# Optional (If you want to return the actual pairs instead):
def solution(a, k):
    result = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if (a[i] + a[j]) % k == 0:
                result.append((a[i], a[j]))
    return result
# Example usage:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(solution(a, k))  # Output: [(1, 2), (1, 5), (2, 4), (3, 6), (4, 5), (6, 9), (7, 8)]
# ===================================
# Task:
# You're given a list of integers.
# Return the number of even numbers in the list.
# a = [1, 2, 3, 4, 5, 6]  → Output: 3

def count_even(a):
   count_odd = 0
   count_even = 0
   for i in range(len(a)):
      if a[i] %2 ==0:
         count_even +=1
      else:
         count_odd += 1
   return (count_even, count_odd)
print(count_even([1, 2, 3, 4, 5, 6, 7]))  # Output: 3 ✅
# if want to return even and odd
def count_even(a):
   count_odd = []
   count_even = []
   for i in range(len(a)):
      if a[i] %2 ==0:
         count_even.append(a[i])
      else:
         count_odd.append(a[i])
   return (count_even, count_odd)
print(count_even([1, 2, 3, 4, 5, 6, 7]))

# Task 1.3 – Count Numbers Greater Than 10



# Type 1 – Accumulate sum

def sum_numbers(a):
    total = 0

    for i in range(len(a)):
        total += a[i]  # add each number

    return total
print(sum_numbers([1, 2, 3, 4]))  # Output: 10

# Task 1: Reverse a String
# Type: 1️⃣ – Simple logic (just loop and build string)
# Goal: Given a string, return its reverse.

def reverse_string(s):
   reversed = ""
  # go through each character from the end to the start
   for i in range(len(s)-1, -1, -1):
      reversed += s[i]  # add current character to result
   return reversed   
         # Initialize an empty string to store the reversed result
print(reverse_string("apple"))   # Output: "elppa"
print(reverse_string("banana"))  # Output: "ananab"

#  Task 2 – Remove Duplicates from a String
# Type: 1️⃣ – Simple logic
# Goal: Given a string, return a new string with all duplicate characters removed, but keep the first occurrence of each character.
# 📝 Example:
# Input:  "banana"  
# Output: "ban"  ✅ ('a' and 'n' are kept only once)

def remove_duplicates(s):
   newstring = ""
   for char in s:
      if char not in newstring:
         newstring += char
   return newstring
print(remove_duplicates("banana"))  # Output: "ban"
print(remove_duplicates("apple"))   # Output: "aple"


# 4. Can we improve the remove duplicates task to ignore numbers/symbols?
# Yes! That’s a CodeSignal-style upgrade!

# 📝 New Task:
# Remove duplicates, only for alphabet letters, and ignore numbers/symbols.

def remove_duplicates_letters_only(s):
    result = ""  # only letters, no repeats

    for char in s:
        # Check if it's a letter (a–z or A–Z)
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            if char not in result:
                result += char  # keep first time only

    return result

print(remove_duplicates_letters_only("banana3r4e7uu"))  # Output: "banrue" ✅ 

# Example: Multiply All Numbers in a List
# Type 1 – Basic Math
def multiply_numbers(a):
    product = 1  # start from 1, not 0
    for i in range(len(a)):
      product *= a[i]  # multiply each number
    return product
print(multiply_numbers([2, 3, 4]))  # Output: 24


# ✅ Task 3 – Check if Two Strings Are Anagrams
# Type: 1️⃣ – Simple logic (no dicts, just loops)
# Goal: Two strings are anagrams if they contain the same letters, but in a different order.

# Count letters in the first string (manually)

# Check if the second string has same letters and same counts

# Input: "listen", "silent"  → ✅ True  
# Input: "apple", "papel"    → ✅ True  
# Input: "hello", "world"    → ❌ False

def is_anagram(s1, s2):
   if len(s1) != len(s2):
      return False    # different lengths, can't be anagrams
   
   counts1 = 0 * 26   # 26 letters a–z
   counts2 = 0 * 26
   
   for i in range(len(s1)):
      index =ord(s1[i]) - ord('a') # convert letter to index 0–25
      counts1 += 1
      for i in range(len(s2)):
         index = ord(s2[i]) - ord('a')   
         counts2 += 1
     # compare both counts
      for i in range(26):
         if counts1[i] != counts2[1]:
            return False      

# Task – Count Vowels in a String
# Type: 1️⃣ – Simple logic
# Goal: Given a string, return the count of vowels (a, e, i, o, u) in it.      

 # List of vowels (both lowercase and uppercase)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 
def vowel_count(s):
    count =0
    vowellist =[]

    for wovel in s:
       if wovel in vowels:
          count += 1     #first line: just increase count
          vowellist.append(wovel)  # second line: add vowel to list
    return (count, vowellist)

print(vowel_count("banana"))  # Output: 3 (a, a, a)
print(vowel_count("apple"))   # Output: 2 (a, e)

# Task 4 – Find the Missing Number from 1 to N
# Type: 1️⃣ Simple Math Logic

# 🧠 Given numbers from 1 to N in a list, with one number missing — find it.
# Input: [1, 2, 4, 5] → Output: 3

def find_missing(a):
   n = len(a) + 1  # N is length of list + 1 (because one number is missing)
   total = n * (n + 1) // 2  # Sum of first N numbers formula: N * (N + 1) / 2
   current_sum = 0  # Sum of numbers in the list
   for num in a:
        current_sum += num  # Add each number in the list
   return total - current_sum  # The missing number is the difference
print(find_missing([1, 2, 4, 5]))  # Output: 3

# Task 5 – Two Sum Problem
# Type: 1️⃣ Simple nested loop

# 🧠 Find two numbers that add up to a target.