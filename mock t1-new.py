# ✅ Task (Type 1 – Simple Logic)
# Given a list of integers, return a new list where each number is replaced with:
# 1 if the number is odd
# 0 if the number is even

#  Example:
# numbers = [4, 7, 10, 3, 8]
# Output: [0, 1, 0, 1, 0]

def solution(numbers):
  result = []
  for number in numbers:
    if number% 2 == 0:
      result.append(0)
    else:
      result.append(1)
  return result

print(solution([4, 7, 10, 3, 8]))      

# 🔢 Mock Test 1: Positive or Negative
# Task:
# Given a list of integers, return a list where:
# 1 if the number is positive
# -1 if the number is negative
# 0 if the number is zero
# Example:
# Input: [5, -3, 0, 8, -1]  
# Output: [1, -1, 0, 1, -1]
def solution(numbers):
  result = []
  for number in numbers:
    if number >= 1:
      result.append(1)
    elif number < 0:
        result.append(-1)
    else:
       number == 0
       result.append(0)
  return result
print(solution([5, -3, 0, 8, -1]))   

# 📏 Mock Test 2: Count digits
# Task:
# Given a list of integers, return a list of the number of digits in each number. (Ignore minus signs.)
# Example:
# Input: [5, 23, 100, -9]  
# Output: [1, 2, 3, 1]

#       the question doesn't say "use 10 to the power of i".
# But we use 10 ** i as a simple trick to check how many digits
#  a number has — without converting to a string or using while loop.
def solution(numbers):                     # define the function
    result = []                            # make an empty list to store answers
    for number in numbers:                 # loop through each number in the list
        if number < 0:                     # if number is negative
            number = -number               # make it positive (remove minus sign)

        count = 0                          # set digit counter to 0
        if number == 0:                    # special case: if number is zero
            count = 1                      # set count to 1 (because 0 has 1 digit)
        for i in range(10):                # loop from i = 0 to 9
            if number >= 10 ** i:          # if number is bigger than or equal to 10^i
                count = i + 1              # then the digit count is i + 1
        result.append(count)               # add the count to result list
    return result                          # return the final result list

# Example use
print(solution([0, 23, 100, -9]))          # Output: [1, 2, 3, 1]

# 📏 Mock Test: Count Digits – Includes 0 and Negative Numbers
# Task:
# Write a function that takes a list of integers and returns a list of digit counts for each number.
# 👉 Ignore the minus sign (-), and remember that 0 counts as 1 digit.

# 🧪 Example:
# Input: [0, -7, 123, -4567, 89]
# Output: [1, 1, 3, 4, 2]

def solution(numbers):
    result = []
    for number in numbers:
      if number < 0:
         number = -number
         count = 0
      if number == 0:
         count = 1
      for i in range(10):
        if number >= 10**i:
           count = i + 1
      result.append(count)
    return result     
print(solution([6, 0, 23, 10044, -9]))          # Output: [1, 2, 3, 1]


# ✅ Task (Type 1 – Simple Logic)
# Given a list of integers, return a new list where each number is replaced with:

# 1 if the number is odd

# 0 if the number is even

# 🧪 Example:
# numbers = [4, 7, 10, 3, 8]
# Output: [0, 1, 0, 1, 0]

def solution(numbers):
  evencount = 0
  oddcount = 0
  result = []
  for num in numbers:
    if num %2 == 0:
      result.append(0)
      evencount += 1
    else:
      result.append(1)
      oddcount += 1  
  return (result, oddcount, evencount) 

print(solution([4, 7, 10, 3, 8]))     



# 🔄 Mock Test 3: Flip 0 and 1
# Task:
# Given a list containing only 0s and 1s, return a list with all values flipped (0 → 1 and 1 → 0).

# Example:
# Input: [1, 0, 1, 1, 0]  
# Output: [0, 1, 0, 0, 1]
def solution(numbers):
   result=[]
   for num in numbers:
      if num == 0:
       result.append(1)
      elif num == 1:
         result.append(0)
   return result
print(solution([0, 0, 0, 1, 0, 0, 1]))         

# 🧪 Task 1
# You are given a list of integers.
# Return a new list where each number is replaced with 1 if it is divisible by 3, and 0 otherwise.

# Example:
# For numbers = [3, 5, 9, 10, 12],
# the output should be [1, 0, 1, 0, 1].

def solution(numbers):
   result = []
   for num in numbers:
      if num % 3 == 0:
         result.append(1)
      else:
         result.append(0)  
   return result
print(solution([3, 5, 9, 10, 12]))        

# 🧪 Task 2
# You are given a list of integers.
# For each number, return 1 if it ends in an even digit, otherwise return 0.

# Example:
# For numbers = [14, 23, 77, 88, 91],
# the output should be [1, 0, 0, 1, 0].

def solution(numbers):
   result= []
   for i in range(len(numbers)):
    # for last digit. This gives you the rightmost digit (ones place).
      endnum = numbers[i] % 10 
      if endnum % 2 == 0:
         result.append(1)
      else:
         result.append(0)
   return result
print(solution([14, 23, 77, 88, 91]))    
      
# 🧪 Task 3
# You are given a list of integers.
# Return a new list where each number is replaced with the number of digits it has.
# Negative signs must be ignored.
# If the number is 0, count it as 1 digit.

# Example:
# For numbers = [-5, 0, 23, 456, -7890],
# the output should be [1, 1, 2, 3, 4].
def solution(numbers):
   result =[]
   for num in numbers:
      if num < 0:
         num= -num
      count = 0
      if num == 0:
         count = 1
      for i in range(10):
        if num >= 10 ** i:
           count = i+1
      result.append(count)
   return result 
print(solution([-5, 0, 23, 456, -7890]) )

      

# =============================================
# =======================================================

# ✅ Task: For each number, return:
# How many digits it has

# A list of its digits (right to left)

# Result for this input:
# [-5, 0, 23, 456, -7890]
# ✅ Output:
# [[1, [5]], [1, [0]], [2, [3, 2]], [3, [6, 5, 4]], [4, [0, 9, 8, 7]]]
# ✅ What it means:
# Each sublist is [count, [digits]]

# ✅ Code Explanation (line by line):
def analyze_digits(numbers):                   # define the function
    results = []                               # list to store final results

    for num in numbers:                        # loop through each number
        if num < 0:                            # if number is negative
            num = -num                         # make it positive

        digits = []                            # to store the digits
        count = 0                              # to count how many digits

        if num == 0:                           # special case for 0
            digits.append(0)                   # 0 has one digit: 0
            count = 1

        else:                                  # for all other numbers
            for i in range(10):                # up to 10 digits (safe limit)
                if num >= 10 ** i:             # if num is bigger than 10^i
                    count = i + 1              # that means we have at least i+1 digits
# to find what is each digit from right to left
            for i in range(count):             # get each digit from right to left
                digit = (num // (10 ** i)) % 10  # math trick to isolate each digit
                digits.append(digit) 

        results.append([count, digits])        # store [digit count, digits] in the final result

    return results                             # return the final list
print(analyze_digits([-5, 0, 23, 456, -7890]))
#  Output:
# [[1, [5]], [1, [0]], [2, [3, 2]], [3, [6, 5, 4]], [4, [0, 9, 8, 7]]]


# ====================================
# *****************************************
      #  string
# ======================================

# ["buy", "sell", "hello", "wow", "fizz", "zoo", "sue", "go", "hey"]

# task wants to return six things:

# ✅ Total number of letters in each word
# ✅ Unique letters (no duplicates)
# ✅ Reversed version of each word (like 'buy' → 'yub')
# ✅ Words that are palindromes (same forward and backward)
# ✅ Words with 'z' replaced by 'z2'
# ✅ Words where every letter moves 3 letters forward (except 'a' → +2)

# Example Output (short summary):

# [
#  [3, 4, 5, 3, 4, 3, 3, 2, 3],                       # letter counts
#  [['b','u','y'], ['s','e','l'], ...],               # unique letters
#  ['yub', 'lles', 'olleh', 'wow', ...],              # reversed
#  ['wow'],                                           # palindromes
#  ['buy', 'sell', 'hello', 'wow', 'fiz2z2', ...],    # z → z2
#  ['ex|', 'vhoo', 'khoor', 'zrz', 'il}}', ...]       # letter shift +3
# ]

def analyze_words(words):
    letter_counts = []        # list to hold how many letters each word has
    letters_per_word = []     # list of unique letters for each word
    reversed_words = []       # reversed version of each word
    palindromes = []          # words that are same forwards and backwards
    z_replaced_words = []     # words where each 'z' is replaced by 'z2'
    shifted_words = []        # words with letters moved forward (a → c, others → +3)

    for word in words:            # loop over each word
        count = 0                 # count letters
        seen_letters = []         # hold unique letters
        reversed_word = ''        # build reversed word
        z_word = ''               # build word with z replaced
        shifted_word = ''         # build shifted word

        for letter in word:       # count letters and find unique letters
            count += 1
            if letter not in seen_letters:
                seen_letters.append(letter)

                   # range(start, stop, step)
        for i in range(len(word) - 1, -1, -1):  # reverse the word manually
            reversed_word += word[i]

        if word == reversed_word:              # check for palindrome
            palindromes.append(word)

        for letter in word:                    # replace z with z2
            if letter == 'z':
                z_word += 'z2'
            else:
                z_word += letter

        for letter in word:                    # shift letters
            if letter == 'a':
                shifted = chr(ord(letter) + 2)  # a → c
            else:
                shifted = chr(ord(letter) + 3)  # all others → +3
            shifted_word += shifted

        # Save results for this word
        letter_counts.append(count)
        letters_per_word.append(seen_letters)
        reversed_words.append(reversed_word)
        z_replaced_words.append(z_word)
        shifted_words.append(shifted_word)

    return [
        letter_counts,
        letters_per_word,
        reversed_words,
        palindromes,
        z_replaced_words,
        shifted_words
    ]
# Print results one by one
# print("Letter counts:", letter_counts)
# print("Unique letters per word:", letters_per_word)
# print("Reversed words:", reversed_words)
# print("Palindromes:", palindromes)
# print("Z replaced words:", z_replaced_words)
# print("Shifted words (+3 or +2 for 'a'):", shifted_words)

# Example input
print(analyze_words(["buy", "sell", "hello", "wow", "fizz", "zoo", "sue", "go", "hey"]))







# Replace the last digit of the number with last digit + 2, for any number length…
def solution(numbers):
   result = []
   for num in numbers:
      lastdigit = num % 10
      firstdigit = num // 10
      newnum = (firstdigit * 10)+(lastdigit+2) # any number length
      # newnum = (firstdigit)+(lastdigit+2) #if just 2 digit
      result.append(newnum)
   return result   

# You are given a list of lowercase words.

# For each word in the list, return 1 if the last letter of 
# the word is a vowel (a, e, i, o, u), and 0 otherwise.

# Return the result as a list of integers.
# Example:
# For words = ["apple", "code", "hi", "yes", "run", "go"]

# The output should be: [1, 1, 1, 0, 0, 1]
vowels=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'o', 'u')
def solution(words):
    vowels = ('a', 'e', 'i', 'o', 'u')
    result = []
    for word in words:
        if word[-1] in vowels:
            result.append(1)
        else:
            result.append(0)
    return result

print(solution(["apple", "code", "hi", "yes", "run", "go"]))
       
def solution(vowels):
   result =[]
for vowel in vowels:
   
   vowel=vowel -1
   if vowel in vowels:
      result.append(vowel)