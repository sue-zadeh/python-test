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
print(solution([1, 2, 1, 3, 4]))  # Output: [1, 1, 0]
    
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
        if part in words:
            return True  # at least one part is not in list

    return False  # all parts matched

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
        return False  # different lengths can't be anagrams

    counts1 = [0] * 26  # 26 letters from 'a' to 'z'
    counts2 = [0] * 26

    # Count letters in s1
    for i in range(len(s1)):
        index = ord(s1[i]) - ord('a')  # convert letter to index 0–25
        counts1[index] += 1            # add 1 to that index

    # Count letters in s2
    for i in range(len(s2)):
        index = ord(s2[i]) - ord('a')  # same for s2
        counts2[index] += 1

    # Compare both count arrays
    for i in range(26):
        if counts1[i] != counts2[i]:  # if count doesn't match
            return False

    return True  # all counts matched

# Task – Count Vowels in a String
# Type: 1️⃣ – Simple logic
# Goal: Given a string, return the count of vowels (a, e, i, o, u) in it.      

 # List of vowels (both lowercase and uppercase)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 
def vowel_count(s):
    count =0
    result =[]

    for wovel in s:
       if wovel in vowels:
          count += 1     #first line: just increase count
          result.append(wovel)  # second line: add vowel to list
    return (count, result)

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
# Input: [2, 7, 11, 15], target = 9  
# → Output: (2, 7)
def two_sum(a, target):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):  # ensure i < j
            if a[i] + a[j] == target:  # check if they add up to target
                return (a[i], a[j])  # return the pair found
    return None  # if no pair found

#  Task 6 – Majority Element
# Type: 1️⃣ Count logic manually
# 🧠 Return the number that appears more than n/2 times.
# Input: [3, 3, 4, 2, 3] → Output: 3
def majority_element(a):
 for i in range(len(a)):
    count =0   # reset for each a[i]
    for j in range (len(a)):
       if a[i] == a[j]:
          count += 1
          if count> len(a) //2:
             return (a[i], count)  # return the element and its count
 return (-1 , 0)  # if no majority element found
print(majority_element([3, 6, 6, 6, 6, 6, 6, 6, 4, 2, 3]))  # Output: (6, 7)

# Task 7 – Check if a Number is Prime
# Type 1 – Basic math logic
        # Here's a quick and efficient way to check if a number n is prime:
# we iterate through 2 to the square root of n. If n is divisible by any of these numbers,
# it's not a prime number. If n is not divisible by any of the numbers in the range,'
# ' then it's a prime number.

# Here is how the solution will look like:
def is_prime(n):
    """Function to check if n is a prime number"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))   # True
print(is_prime(10))  # False

#  Task 8 – GCD of Two Numbers
# Type 1 – Use loop to find greatest common divisor
def gcd(a, b):
  result =1
  for i in range(1, min(a,b)+ 1):
     if a % i == 0 and b % i == 0:
        result = i
  return (result, a, b)  # return the greatest common divisor found


print(gcd(12, 18))  # Output: 6

# Task 9 – Valid Parentheses
# Type 1 (Simulate Stack using string)
def valid_parentheses(s):
  stack = ""  # simulate stack using string
  for char in s:
     if char =="(":
        stack +=char # push opening bracket
     elif char ==")":
        if stack== '': # if stack is empty
           return False  # if stack is empty, invalid parentheses
        stack = stack[:-1]  # pop last character
  return stack == ""  # if stack is empty, parentheses are valid
print(valid_parentheses("()"))     # True
print(valid_parentheses("()[]{}")) # True
print(valid_parentheses("([{}])")) # True
print(valid_parentheses(")("))     # False
print(valid_parentheses(")("))     # False  
print(valid_parentheses("(())"))   # True
print(valid_parentheses("(()"))    # False


# 4. Implement a Queue using Stacks
# (Still Type 1 because it’s simulation with lists)

# We’ll simulate enqueue (push) and dequeue (pop) with two lists.
# To simulate a Queue (FIFO: First-In, First-Out) behavior using two Stacks (LIFO: Last-In, First-Out).
# We use:
# stack_in for pushing new elements
# stack_out for removing elements in correct order
def queue_simulator(operations, values):
    stack_in = []     # stack to store new items (push here)
    stack_out = []    # stack to reverse items for correct order (pop here)
    result = []       # list to store results of each dequeue

    # loop through all operations
    for i in range(len(operations)):
        if operations[i] == "enqueue":
            # if operation is enqueue, add value to stack_in
            stack_in.append(values[i])

        elif operations[i] == "dequeue":
            # if stack_out is empty, we need to refill it
            if len(stack_out) == 0:
                # move all items from stack_in to stack_out
                for j in range(len(stack_in) - 1, -1, -1):
                    stack_out.append(stack_in[j])  # add item from end of stack_in
                stack_in = []  # clear stack_in after moving all

            # now if stack_out has something, pop and return it
            if len(stack_out) > 0:
                item = stack_out[-1]          # get the last item
                stack_out = stack_out[:-1]    # remove it from stack_out
                result.append(item)           # store it in result
            else:
                # if both stacks are empty, nothing to return
                result.append(None)

    return result  # return final results list


ops = ["enqueue", "enqueue", "enqueue", "dequeue", "dequeue"]
vals = [1, 2, 3, None, None]

print(queue_simulator(ops, vals))  # Output: [1, 2]


# ✅ Type 1 – Mock Exam Question
# 💻 Task: Count Numbers Greater Than Average
# Type: 1️⃣ – Simple Logic (no advanced tools)
# Time Limit: ⏱️ 10 minutes (but you can do it faster!)
# Loop: Only use for loops
# Goal:
# Given a list of integers, return the number of values greater than the average of all numbers in the list.

# 📝 Example:
# Input: [1, 2, 3, 4, 5]  
# → Average is 3  
# → Numbers greater than 3: [4, 5]  
# → Output: 2
def count_greater_than_average(numbers):
    result = []  # to collect numbers greater than average
    total = 0    # to store the sum of numbers

    # Step 1: calculate the sum
    for i in range(len(numbers)):
        total += numbers[i]

    # Step 2: calculate the average
    average = total // len(numbers)  # integer division

    # Step 3: collect all numbers greater than average
    for i in range(len(numbers)):
        if numbers[i] > average:
            result.append(numbers[i])

    return result  # return the list of numbers greater than average

print(count_greater_than_average([1, 2, 3, 4, 5]))  # Output: [4, 5]

# ✅ Type 1 – Mock Exam Question 2
# 💻 Task: Count Digits in a String
# 🧠 Type: 1️⃣ – Simple logic, loop-based
# Goal: Given a string s, return how many characters are digits (0–9).

# 📝 Example 1:
# Input:  "abc123xyz"
# Output: 3
# 📝 Example 2:
# Input:  "code@2025!"
# Output: 4
def count_digits(s):
   count = 0
   for char in s:
      if 48 <= ord(char) <= 57: # we can say easier if '0' <= char <= '9':
         count += 1
   return count
print(count_digits("abc123xyz"))  # Output: 3
print(count_digits("code@2025!"))  # Output: 4

# ✅ Type 1 – Mock Exam Question 3
# 💻 Task: Count Lowercase Letters
# 🧠 Type: 1️⃣ – Simple logic
# Goal: Given a string s, return how many characters are lowercase letters (a to z only).

# 📝 Example 1:
# Input: "HelloWorld123"  
# Output: 8  → lowercase: e, l, l, o, o, r, l, d
# 📝 Example 2:
# Input: "PYTHONrocks!"  
# Output: 5  → lowercase: r, o, c, k, s

def count_lowercase(s):
   count = 0
   for char in s:
      if 'a' <= char <= 'z':
         count += 1
   return count
print(count_lowercase("HelloWorld123"))  # Output: 8
print(count_lowercase("PYTHONrocks!"))  # Output: 5

#  Type 1 – Mock Exam Question 4
# 💻 Task: Count Vowels in a String and Return the Vowel List
# 🧠 Type: 1️⃣ – Simple logic
# Goal: Given a string s, return:
# The number of vowels in the string
# A list of the vowels found (in order of appearance)

# 📝 Example 1:
# Input: "CodeSignal"
# Output: (4, ['o', 'e', 'i', 'a'])
# 📝 Example 2:
# pyt
# Input: "xyz"
# Output: (0, [])
def count_vowels(s):
   wovels = ['o', 'e', 'i', 'a', 'I', 'A', 'E', ]
   count =0
   list=[]
   for char in s:
      if "a" <= char <= "z" or "A" <= char <= "Z":
         if char in vowels:
          count += 1
          list.append(char)
   return (count, list)
print(count_vowels("CodeSignal"))


# ✅ Type 1 – Mock Exam Question 5
# 💻 Task: Count Capital Letters in a String
# 🧠 Type: 1️⃣ – Simple logic
# Goal: Return how many characters in the string are uppercase letters (A to Z only)

# 📝 Example:
# Input: "CodeSIGNAL2025!"
# Output: 7  → ['C', 'S', 'I', 'G', 'N', 'A', 'L']
def solution(s):
  count = 0
  capital_list = []
  for char in s:
    if "A" <= char <= "Z":
      count += 1
      capital_list.append(char)
  return (count, capital_list )   
print(solution('CodeSIGNAL2025!'))  

# ✅ Type 1 – Mock Exam Question 6
# 💻 Task: Count Even Numbers in a List
# 🧠 Type: 1️⃣ – Simple logic
# Goal: Return the number of even numbers in the list

# 📝 Example:
# Input: [1, 4, 7, 8, 10]
# Output: 3   → (4, 8, 10)

def solution(num):
   count_even = 0
   count_odd = 0
   list_even=[]
   list_odd=[]
   for char in num:
      if char % 2 == 0:
         count_even += 1
         list_even.append(char)
      else:
         count_odd += 1
         list_odd.append(char)
   return(count_even, count_odd, list_even, list_odd)    
print(solution([1,2,3,4,5,6,7,8,9]) )     

# ✅ Type 1 – Mock Exam Question 7
# 💻 Task: Count Uppercase and Lowercase Letters in a String
# 🧠 Type: 1️⃣ – Basic string loop
# Goal: Return how many uppercase and lowercase letters are in the input string

# 📝 Example:
# Input: "HeLLoWorld123!"
# Output: (5, 5)  # 5 uppercase, 5 lowercase
def solution(s):
   count_upper = 0
   count_lower = 0
   list_upper = []
   list_lower = []
   for char in s:
      if "a" <= char <= "z":
         count_lower += 1
         list_lower.append(char)
      elif "A" <= char <= "Z":
         count_upper += 1
         list_upper.append(char)
   return(count_upper, count_lower, list_upper, list_lower) 
print(solution("HeLLoWorld123!"))      

# ✅ Type 1 – Mock Exam Question 8
# 💻 Task: Count Characters by Category
# 🧠 Type: 1️⃣ – Multi-condition logic
# Goal: Return how many letters, digits, and special characters are in the string

# 📝 Example:
# Input: "Code@2025!"
# Output: (4, 4, 2)
# # 4 letters: C, o, d, e
# # 4 digits: 2, 0, 2, 5
# # 2 specials: @, !
# You should:

# Use only for loops
# No built-ins like .isalpha(), .isdigit(), etc
# Rely on ASCII ranges
def solution(s):
   count_digit = 0
   count_letter = 0
   count_special = 0
   for char in s:
      if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
         count_letter += 1
      elif 48 <= ord(char) <= 57:
         count_digit += 1
      else:
         count_special +=1
   return(count_letter, count_digit, count_special)   
print(solution("Code@2025!"))         

