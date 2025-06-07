for i in range(1,100):
    if i%3==0 and i%5==0:
        print("sss")
    elif i % 5== 0:
        print("ww")
    else:
        print(i)
# # =======================
def transition_array(a):
            b=[]
            for i in range(len(a)):
                if i==0 or  a[i-1] % 2 == 0:
                    b.append(a[i])
                else:
                    b.append(a[i] + 1)
            return b
# # #         # ===============
count = 0
k=3
a = [1, 2, 3, 4, 5]
for i in range(len(a)):
 for j in range (i+1, len(a)):
     if (a[i] +a[j]) % k ==0:
         count+=1
print(count)

# # # =====
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
k=5
for i in range (len(a)):
     for j in range (i+1, len(a)):
          if (a[i] + a[j]) % k ==0:
            count+=1
print(count)

# # ==========================
# # Try this:

# # Given an array a, return an array b where:
# # b[i] = a[i] * 2 if a[i] is even, otherwise b[i] = a[i] + 1

# # Example input:
# # a = [2, 3, 4, 5]
# # Expected output:
# # b = [4, 4, 8, 6]

# # Give it a try. You can use .append() and for loop. Let me know if you want a small hint 😄 You're doing so good!
a = [2, 3, 4, 5]
b = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i] * 2)
    else:
        b.append(a[i] + 1)
print(b)  # Output should be: [4, 4, 8, 6]


c=[4,5,2,3,6,2]
def solution (c):
    b=[]
    for i in range (len(c)):
        if a %2==0:
            b.append(c[i]*2)
        else:
            b.aapend(c[i] + 1)
    return b # output should be [8, 6, 4, 4, 12, 4]
    


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
# //Write a function that takes a string s, iterates through it, 
# and collects all 0-based positions of vowels in it to a list.

# Note that you should not use any Python built-in string methods to solve this task.

# For example, print(solution("Hello WORLD")) should output [1, 4, 7]. 
# Here, 'e' is a vowel, and its position in the string "Hello" is 1. 'o' is also a vowel,
#  and its position is 4. The last vowel is O at position 7.

def solution(s):
    # TODO: implement find_vowels_positions
    vowel=['i','o','e','u','a','I','O','E','U','A']
    vowelCont=[]
    for i in range (len(s)):
        char = s[i]
        if char in vowel:
         vowelCont.append(i)    
    return vowelCont
# ==========================
# Given a string, you need to return a new string where every letter is shifted 
# to its right by one place in alphabetical order. The last letters z and Z should be
# replaced with the first ones: a and A, respectively. If the character isn't a letter,
#  it should stay the same.

# It is not allowed to use string built-in methods here.

# For example, given the string "abc123XYz!", the function should return "bcd123YZa!".

def solution(s):
    result = []

    for i in range(len(s)):
        char = s[i]

        # Lowercase letters
        if 97 <= ord(char) <= 122:
            if char == 'z':
                result.append('a')
            else:
                result.append(chr(ord(char) + 1))

        # Uppercase letters
        elif 65 <= ord(char) <= 90:
            if char == 'Z':
                result.append('A')
            else:
                result.append(chr(ord(char) + 1))

        # Non-letters stay the same
        else:
            result.append(char)

    return ''.join(result)

#============
# Task:
# Write a function that takes a string s and returns a new string where:

# Each letter is shifted forward by 2 letters in the alphabet.

# 'y' → 'a', 'z' → 'b', 'Y' → 'A', 'Z' → 'B'

# Non-letter characters stay the same.

# ✅ Example:

# solution("aBz123!") ➜ "cDd123!"
# solution("XYz!")    ➜ "ZBa!"
# solution("hello")   ➜ "jgnnq"

def solution(s):
    result=[]
    for i in range(len(s)):
        char=s[i]
        if 97<=ord(char) <=122:
            if char=='y':
                result.append('a')
            elif char=='z':
                result.append('b')
            else: 
                result.append(chr(ord(char)+2))
        elif 65<= ord(char)<=90:
            if char=='Z':
                result.append('B')
            elif char=='Y':
                result.append('A')
            else:
                result.append(chr(ord(char)+2))
        else:
                result.append(char)
    return ''.join(result)
print(solution("aBz123!"))  # ➜ "cDb123!"
print(solution("XYz!"))     # ➜ "ZAb!"
print(solution("hello"))    # ➜ "jgnnq"
#================================

# Challenge 2: Shift Every Letter Backward by 1
# ❓Task:
# Same as above, but shift letters backward by 1

# 'a' → 'z', 'A' → 'Z'

# Non-letters stay the same

# ✅ Example:
# python
# Copy code
# solution("bC1!") ➜ "aB1!"
# solution("aA")   ➜ "zZ"
# solution("jgnnq") ➜ "hello"

def solution(s):
    result=[]
    for i in range(len(s)):
        char=s[i]
        if 97<=ord(char)<=122:
            if char=="a":
                result.append('z')
            else:
                result.append(chr(ord(char)-1))
        elif 65<= ord(char) <=90:
              if char=="A":
               result.append("Z")
              else:
                  result.append(chr(ord(char)-1))
        else:
          result.append(char)
    return ''.join(result)
print(solution("bC1!"))     # ➜ "aB1!"
print(solution("aA"))       # ➜ "zZ"
print(solution("jgnnq"))    # ➜ "ifmmp"
# ==========================
# Challenge 3: Shift by 3 — Vowels Only
# ❓Task:
# Only shift vowels (a, e, i, o, u, A, E, I, O, U)
#  forward by 3 letters

# If it's 'u' → 'x', 'U' → 'X'

# Other letters and non-letters stay the same

# ✅ Example:
#  solution("aBecID") ➜ "dBhcLG"
#  solution("hello!") ➜ "hgnno!"
def solution(s):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    result = []

    for char in s:
        if char in vowels:
            result.append(chr(ord(char) + 3))
        else:
            result.append(char)

    return ''.join(result)



print(solution("aBecID"))   # Output: "dBhcLG"
print(solution("hello!"))   # Output: "hgnno!"
#=====================
# LEVEL 1 – Practice With Basic Shifting
# ✅ Task 1: Shift All Letters Forward by 2
# Rules:

# 'a' → 'c', 'y' → 'a', 'z' → 'b'

# 'A' → 'C', 'Y' → 'A', 'Z' → 'B'

# Keep other characters the same

# 🧪 Example:

# python
# Copy code
# solution("Zoo!") ➜ "Bqq!"

def solution(s):
    result = []
    for i in range(len(s)):
        char = s[i]
        if 97 <= ord(char) <=122:
            if char=="a":
                result.append("c")
            elif char == "y":
                result.append("a")
            elif char == "z":
                result.append("b")
            else:
                result.append(chr(ord(char)+2))

        elif 65 <= ord(char) <=90:
            if char=="A":
               result.append("C")
            elif char=="Y":
                result.append("A")
            elif char== "Z":
                result.append("B")
            else:
               result.append(chr(ord(char)+2))
    else:
         result.append(char)
    return ''.join(result)
print(solution("Zoo!"))  # Output: "Bqq!"

# ✅ Task 2: Shift All Letters Backward by 2
# Rules:
# 'c' → 'a', 'a' → 'y', 'b' → 'z'
# 'C' → 'A', 'A' → 'Y', 'B' → 'Z'
# Keep other characters the same
# solution("Bqq!") ➜ "Zoo!"

def solution(s):
    result= []
    for char in s:
        if 97 <= ord(char) <= 122:
            if char == "c":
             result.append("a")
            elif char=="b":
              result.append("z")
            elif char =="a":
              result.append("y")
            else:
                result.append(chr(ord(char) - 2))
        elif 65 <= ord(char) <= 90:
            if char == "C":
              result.append("A")
            elif char == "B":
               result.append("z")
            elif char == "A":
                result.append("Y")
            else:
                result.append(chr(ord(char) - 2))

    else:
          result.append(char)
    return "".join(result)            

print(solution("Bqq!"))  # Output: "Zoo!"
# ==============================

# ===========================
# befor this i want to solve another task:
#  get any string and show just wovels in a new array

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
def solution(s):
    result = []

    for char in s:
        if char in vowels:
         result.append(char) 
    return result  
print(solution("Hello World!"))  # Output: ['e', 'o', 'o']              
# =====================================

# Task:
# Write a function that takes:

# A string s

# A list of target letters (e.g. ['a', 'b', 'e'])

# And returns a list of [letter, count] only for letters that appear at least once in the string.

# 🚫 You are not allowed to use .count() or collections.Counter.

# ✅ Example:

# Input: s = "alphabet banana", targets = ['a', 'b', 'e']
# Output: [['a', 5], ['b', 2], ['e', 1]]
targets = ['a', 'b', 'e']
def solution(s):
    result = []
    
    for target in targets:
      count = 0
      for char in s:
                if char == target:
                    count += 1
      if count > 0:
           result.append([target, count])
    return result
print(solution("alphaaaa teee"))  # Output: [['a', 5], ['b', 2], ['e', 1]]
#===============================

# PART 2: New Task — Count ALL repeated letters in a string
# Show only letters (ignore spaces, punctuation)
# And show how many times each letter is repeated (if count ≥ 2)

# 🧠 Example:

# Input: "hello world"
# Output: [['l', 3], ['o', 2]]

def solution(s):
    result = []
    checked = []
    for letter in s:
        if not letter.isalpha():
            continue
        if letter in checked:
            continue 
        count = 0
        for char in s:
                if char == letter:
                    count += 1
        if count>= 2:
            result.append([letter, count])
        checked.append(letter)
    return result
print(solution("hello world heyyy rrddd"))  # Output: [['l', 3], ['o', 2]] 

# =================================

# Given a string input_string, return a new string in which all
#  occurrences of character c1 in the original string replaced by c2.
#  You cannot use any built-in string methods or functions in Python, such as replace().

# Here's an example:

# print(replace_character("hello, world", "o", "a"))  
# # Output: "hella, warld"
# In this example, all occurrences of o have been replaced by a.


                
for i in range(1,100):
    if i%3==0 and i%5==0:
        print("sss")
    elif i % 5== 0:
        print("ww")
    else:
        print(i)
# # =======================
def transition_array(a):
            b=[]
            for i in range(len(a)):
                if i==0 or  a[i-1] % 2 == 0:
                    b.append(a[i])
                else:
                    b.append(a[i] + 1)
            return b
# # #         # ===============
count = 0
k=3
a = [1, 2, 3, 4, 5]
for i in range(len(a)):
 for j in range (i+1, len(a)):
     if (a[i] +a[j]) % k ==0:
         count+=1
print(count)

# # # =====
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
k=5
for i in range (len(a)):
     for j in range (i+1, len(a)):
          if (a[i] + a[j]) % k ==0:
            count+=1
print(count)

# # ==========================
# # Try this:

# # Given an array a, return an array b where:
# # b[i] = a[i] * 2 if a[i] is even, otherwise b[i] = a[i] + 1

# # Example input:
# # a = [2, 3, 4, 5]
# # Expected output:
# # b = [4, 4, 8, 6]

# # Give it a try. You can use .append() and for loop. Let me know if you want a small hint 😄 You're doing so good!
a = [2, 3, 4, 5]
b = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i] * 2)
    else:
        b.append(a[i] + 1)
print(b)  # Output should be: [4, 4, 8, 6]

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
def solution(a):
    b=[]
    for i in range(len(a)):
        if a[i] % 2 == 0:
            b.append[a[i]]
        else:
           if a[i] % 2 != 0:
            b.append(a[i] + a[i-1]) 
    return b
print(solution([2, 5, 4, 7, 8], []))  # Output: [2, 7, 4, 11, 8]

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
