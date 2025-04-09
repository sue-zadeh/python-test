# # for i in range(1,100):
# #     if i%3==0 and i%5==0:
# #         print("sss")
# #     elif i % 5== 0:
# #         print("ww")
# #     else:
# #         print(i)
# # =======================
# def transition_array(a):
#             b=[]
#             for i in range(len(a)):
#                 if i==0 or  a[i-1] % 2 == 0:
#                     b.append(a[i])
#                 else:
#                     b.append(a[i] + 1)
#             return b
# # #         # ===============
# count = 0
# k=3
# a = [1, 2, 3, 4, 5]
# for i in range(len(a)):
#  for j in range (i+1, len(a)):
#      if (a[i] +a[j]) % k ==0:
#          count+=1
# print(count)

# # # =====
# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# k=5
# for i in range (len(a)):
#      for j in range (i+1, len(a)):
#           if (a[i] + a[j]) % k ==0:
#             count+=1
# print(count)

# # ==========================
# # Try this:

# # Given an array a, return an array b where:
# # b[i] = a[i] * 2 if a[i] is even, otherwise b[i] = a[i] + 1

# # Example input:
# # python
# # Copy
# # Edit
# # a = [2, 3, 4, 5]
# # Expected output:
# # python
# # Copy
# # Edit
# # b = [4, 4, 8, 6]
# # Give it a try. You can use .append() and for loop. Let me know if you want a small hint 😄 You're doing so good!
# a = [2, 3, 4, 5]
# b = []
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         b.append(a[i] * 2)
#     else:
#         b.append(a[i] + 1)
# print(b)  # Output should be: [4, 4, 8, 6]

# =======================

a = [2, 3, 4, 5]
b=[]
for i in range(len(a)):
   
    left = a[i - 1] if i - 1 >= 0 else 0
    right = a[i + 1] if i + 1 < len(a) else 0

    b.append(left + a[i] + right)
print(b)  # 👉 should give [5, 9, 12, 9]

# ==============
a = [3, 1, 4, 4, 2, 3, 5, 1]
b = []
for i in a:
    if i not in b:
        b.append(i)
        b.sort(reverse=True)
print(b)  # Output should be: [3, 1, 4, 2, 5]
# ==========================
sentence = "I love learning and I love Python"
words=sentence.split()
counts = {}
# word_count = 0
for word in words:
     if word in counts:
        # word_count+= 1
        counts[word] += 1
     else:
        
        counts[word] = 1
print(counts)
# =======================
a= [1, 2, 3, 4, 5]
b = []
for num in a:
    if num % 2 == 0:
        b.append(num) 

print(b)
# Output should be: [2, 4]
# ==========================
input ='Beautiful'
result= ""
vowels = "aeiouAEIOU"

# Output: "Btfl"
# letters = input.split()
for letter in input:
    if letter not in vowels:
        result += letter
print(result)
# Output: "Btfl"
# ==========================
# ✨ Write a Python function that takes a list of integers and returns the second largest number.

def second_largest(numbers):
    sorted_list = sorted(set(numbers))  # remove duplicates
    return sorted_list[-2]  # second largest is at -2

# Test
numbers = [5, 1, 8, 7, 3]
print(second_largest(numbers))  # Output: 7
# ========================
import re

words = ["name", "rule", "is", "date"]
complex = "myNameInDateIs"

# Step 1: Split the camelCase word
split_words = re.findall(r'[A-Z]?[a-z]+', complex)

# Step 2: Convert to lowercase for comparison
split_words = [w.lower() for w in split_words]

# Step 3: Check each word against your list
for w in split_words:
    if w in words:
        print(f" Found: {w}")
    else:
        print(f" Not found: {w}")
# ========================
import re

def check_words_in_camel(words, complex_word):
    # Split the camelCase word into individual words
    parts = re.findall(r'[A-Z]?[a-z]+', complex_word)
    
    # Convert each part to lowercase and check if it exists in words list
    for part in parts:
        if part.lower() not in words:
            return False
    return True
words = ["name", "rule", "is", "date"]
complex_word = "myNameIsDate"

print(check_words_in_camel(words, complex_word))  # Output: False (because 'my' is not in the list)
# ========================
# Write a function that:
# Accepts two arguments:
# words – a list of lowercase words
# complex_word – a single camelCase string
# Splits the camelCase word into individual words
# Checks if all the words from that split are present in the words list
# Returns:
# True if all words are found
# False if any word is not found
import re
lowercase = ["name", "rule", "is", "date"]
complexword = "myNameIsDate"
individualword = re.findall(r'[A-Z]?[a-z]+', complexword)
individualword = [w.lower() for w in individualword]
for w in lowercase:
    if w in individualword:
        print("True")
    else:
        print("False")
# ========================
# Given an array a, return a new array b where each element is:

# b[i] = a[i] if a[i] is even

# b[i] = a[i] + a[i-1] if a[i] is odd

# For the first element, if i = 0, and it’s odd → just keep a[i] (because there is no a[i-1])
a = [2, 5, 4, 7, 8]
b = []
for i in range (len(a)):
    if  a[i] % 2!=0 :
        if a[i] + a[i-1]:
           b.append(a[i] + a[i-1])
    else:
        b.append(a[i] )
print(b)
# =========================
# Task:
# Write a Python function that takes a sentence (string) and returns the longest word in that sentence.
# If there are two or more words with the same length, return the first one that appears.

input=  "I love programming in Python"
def longword (input):
  words = input.split()
  longest = []
  for word in words:
        if len(word) > len(longest):
            longest = word
  return(longest)
print(longword (input) ) 
# ====================
# Write a Python function that:

# Takes a list of integers

# Returns a new list where all consecutive duplicate values are removed
# (but the original order is preserved)
num = [1, 2, 2, 3, 2 ,5 , 4, 4, 5]
def remove_consecutive_duplicates(num):
    newlist = []
    for n in num:
        if not newlist or newlist[-1] != n:
            newlist.append(n)
    return newlist
print(remove_consecutive_duplicates(num)) 
# =====================
# to remove all duplicated numbers:

def remove_all_duplicates(lst):
    newlist = []
    for n in lst:
        if n not in newlist:
            newlist.append(n)
    return newlist

# Test
num = [1, 2, 2, 3, 2, 5, 4, 4, 5]
print(remove_all_duplicates(num))  # Output: [1, 2, 3, 5, 4]
# ==========================
# merging two strings
from collections import Counter

a = "aabjtt"
b = "bcjw"

count_a = Counter(a)
count_b = Counter(b)

i, j = 0, 0
merged = ""

while i < len(a) and j < len(b):
    char_a = a[i]
    char_b = b[j]
    
    freq_a = count_a[char_a]
    freq_b = count_b[char_b]

    if freq_a < freq_b:
        merged += char_a
        i += 1
    elif freq_b < freq_a:
        merged += char_b
        j += 1
    else:
        if char_a < char_b:
            merged += char_a
            i += 1
        elif char_b < char_a:
            merged += char_b
            j += 1
        else:
            # Same char, pick from a
            merged += char_a
            i += 1

# Add leftovers
merged += a[i:]
merged += b[j:]

print(merged)
# ================
