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
#     for i in range(len(result) // 2):
#         if result[i] != result[len(result) - 1 - i]:
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

# You are given a list of integers. Your task is to write a function find_min(nums),
# that returns the minimum number from the list without using Python's built-in min() function.

# If the list is empty, your function should return None.

def find_min(nums):
    if len(nums) == 0:
        return None  # Check for empty list

    min_val = nums[0]  # Start by assuming the first number is the smallest

    for i in range(1, len(nums)):  # Start from the second item
        if nums[i] < min_val:
            min_val = nums[i]  # Update min_val if a smaller number is found

    return min_val
# Example usage:
print(find_min([3, 1, 4, 1, 5, 9]))  # Output: 1

# You are given an array of integers. Your job is to return the count of even 
# and odd integers in the given array without using any built-in Python methods.

# Your function should return a tuple in the format (even_count, odd_count),
# where even_count represents the number of even integers and odd_count 
# represents the number of odd integers in the provided array.

def solution(nums):
 even_count = 0
 odd_count = 0
 for i in range(len(nums)):
   if nums[i] % 2 == 0:
    even_count += 1
   else:
    odd_count += 1
 return (even_count, odd_count)
## Example usage:
print(solution([1, 2, 3, 4, 5]))  # Output: (2, 3)

# return two lists:
# one containing all the even numbers
# one containing all the odd numbers

def solution(nums):
 even_count = []
 odd_count = []
 for i in range(len(nums)):
   if nums[i] % 2 == 0:
    even_count.append(nums[i])
   else:
    odd_count.append(nums[i])
 return (even_count, odd_count)
#example usage:
print(solution([1, 2, 3, 4, 5]))  # Output: ([2, 4], [1, 3, 5])
      
# You are given an array of integers. Your task is to write a function in Python 
# that returns the number of times the smallest element appears in the array.

# Please note that built-in methods such as min() or count() should not be used in this task.
# Your goal is to accomplish this task by iterating over the array elements manually.
# Try to solve the task by doing just a single list traversal.

def count_min(numbers):
    if len(numbers) == 0:
        return 0  # ✅ check empty list FIRST

    smallest = numbers[0]
    count_min = 0  # ✅ define after checking for empty list

    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
            count_min = 1  # reset count
        elif numbers[i] == smallest:
            count_min += 1

    return count_min
print( count_min([3, 1, 2, 1, 4,0  ])) 


# You are given a list of integers. Your task is to write a Python function
# to find the  among these integers. If the list has fewer
# than two unique numbers, return None.

# You are not allowed to use any built-in Python functions or methods such as
# sorted(), max(), or sort(). Instead, you should implement the task using basic list operations.

from typing import List, Optional
def second_max(nums: List[int]) -> Optional[int]:
    if len(nums) < 2:
        return None

    first = nums[0]
    second = None

    for i in range(1, len(nums)):
       
        if nums[i] == first:
            continue  # skip if same as current max

        if nums[i] > first:
            second = first
            first = nums[i]
        elif second is None or (nums[i] > second and nums[i] != first):
            second = nums[i]
    # Handle case: no second unique max found
    if second is None:
        return None
    return second
# Example usage:
print(second_max([3, 1, 2, 4, 5]))  # Output: 4


#======================================

# PART 1: Code for “Find the 3rd Largest Unique Number”
# ❓ Task:
# Given a list of integers, return the third largest unique number in the list.
# If there are fewer than 3 unique numbers, return None.

# 🚫 Don't use: max(), sorted(), or set().

def third_max(nums):
    if len(nums) < 3:
        return None

    first = second = third = None

    for i in range(len(nums)):
        if nums[i] == first or nums[i] == second or nums[i] == third:
            continue

        if first is None or nums[i] > first:
            third = second
            second = first
            first = nums[i]
        elif second is None or nums[i] > second:
            third = second
            second = nums[i]
        elif third is None or nums[i] > third:
            third = nums[i]

    if third is None:
        return None
    return third
print(third_max([5, 3, 1, 2, 4]))        # ➜ 3
print(third_max([9, 9, 9, 9]))           # ➜ None
print(third_max([10, 20]))              # ➜ None
print(third_max([10, 20, 30]))          # ➜ 10

#================================

#  For 2nd smallest and 3rd smallest
# To convert from largest → smallest, just change > to < (and the logic flips).

def second_min(nums):
    if len(nums) < 2:
        return None

    first = nums[0]
    second = None

    for i in range(1, len(nums)):
        if nums[i] == first:
            continue

        if nums[i] < first:
            second = first
            first = nums[i]
        elif second is None or (nums[i] < second and nums[i] != first):
            second = nums[i]

    if second is None:
        return None
    return second


#================================

# 🔹 Example: 3rd smallest


def third_min(nums):
    first = second = third = None

    for i in range(len(nums)):
        if nums[i] == first or nums[i] == second or nums[i] == third:
            continue

        if first is None or nums[i] < first:
            third = second
            second = first
            first = nums[i]
        elif second is None or nums[i] < second:
            third = second
            second = nums[i]
        elif third is None or nums[i] < third:
            third = nums[i]

    if third is None:
        return None
    return third

#================================






#===============================

# Given a list of integers, return a tuple (min_val, max_val) containing the smallest and largest number.
# Don’t use min() or max()

def min_max(nums):
   if len(nums) == 0:
      return None
   min_val = nums[0]
   max_val = nums[0]
   for i in range(1, len(nums)):
      if nums[i] < min_val:
         min_val = nums[i]
      if nums[i] > max_val:
          max_val = nums[i]
   return(min_val, max_val)
# Example usage:
print(min_max([3, 1, 2, 4, 5]))  # Output: (1, 5)

# Given a camelCase string (e.g. "myNameIsSue"), return a list of the lowercase words:
# "myNameIsSue" → ["my", "name", "is", "sue"]

def split_camel_case(s):
    result = []     # Stores the final list of words
    word = ""       # Builds the current word letter-by-letter

    for char in s:  # Go through each letter in the string
        if 65 <= ord(char) <= 90:  # If   it's an uppercase letter (A–Z)
            if word != "":         # If we already have a word (means it ended)
                result.append(word)  # Save the completed word
            word = chr(ord(char) + 32)  # Start new word with lowercase of uppercase
        else:
            word += char           # Add character to current word

    if word != "":                 # After loop ends, add the last word if any
        result.append(word)

    return result

# Example usage:
print(split_camel_case("myNameIsSue"))  # Output: ["my", "name", "is", "sue"]
               
# ========================

#  CamelCase with Index (i)
# Task:
# You are given a string in camelCase format like "myVariableNameInCamel".
# Write a function to split it into separate lowercase words using only ASCII and for i in range(len(s)).

# Output should be:
# ["my", "variable", "name", "in", "camel"]


def split_camel_case_with_index(s):
    result = []     # Final list of words
    word = ""       # Temporary string to build each word

    for i in range(len(s)):       # Loop using index
        char = s[i]               # Get character at current index

        if 65 <= ord(char) <= 90:  # If uppercase (A-Z)
            if word != "":         # If we’ve been building a word
                result.append(word)  # Save it to result
            word = chr(ord(char) + 32)  # Start new word with lowercase letter
        else:
            word += char           # Add char to current word

    if word != "":                 # Add the last word at the end
        result.append(word)

    return result

print(split_camel_case_with_index("myVariableNameInCamel"))
# → ["my", "variable", "name", "in", "camel"]

#================================



#================================

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

# Example usage
print(is_prime(10)) # Outputs: False
print(is_prime(11)) # Outputs: True

# You are given an integer number n. The task is to determine if this number is
# a perfect square or not. A perfect square is a number that can be expressed as 
# the product of an integer with itself. For example, 1 = 1 * 1, 4 = 2 * 2, 9 = 3 * 3, 
# and 16 = 4 * 4 are perfect squares, but 2, 3, 5, and 6 are not.

# Implement a function is_perfect_square(n) that returns True if the given number n is
# a perfect square and False otherwise.

def is_perfect_square(n):
   pass

# You are given an integer number n. The task is to determine if this number 
# is a perfect square or not. A perfect square is a number that can be expressed
# as the product of an integer with itself. For example, 1 = 1 * 1, 4 = 2 * 2, 9 = 3 * 3, 
# and 16 = 4 * 4 are perfect squares, but 2, 3, 5, and 6 are not.

# Implement a function is_perfect_square(n) that returns True if the given number n is
# a perfect square and False otherwise.

def is_perfect_square(n):
    if n < 0:
     return False
    for i in range(int(n**0.5) + 1):
        if i * i == n:
         return True
    return False
# Example usage:
print(is_perfect_square(16))  # Output: True (4 * 4)
print(is_perfect_square(20))  # Output: False (not a perfect square)

# You are given an integer number, 1 ≤ n ≤ 10**6

# Your task is to write a function next_prime(n), that takes an integer n as
# input and returns the smallest prime number larger than n.

# Here are some examples:

# next_prime(7) should return 11, because 11 is the next prime number after 7.
# next_prime(13) should return 17, because 17 is the next prime number after 13.
# next_prime(50) should return 53, because 53 is the next prime number after 50.
def next_prime(n):
    for nextprime in range(n + 1, n * 2):  # Look ahead safely up to n*2
        is_prime = True                   # Assume it's prime unless proven wrong

        for i in range(2, int(nextprime ** 0.5) + 1):  # Check divisibility
            if nextprime % i == 0:
                is_prime = False          # Not prime
                break                     # No need to check more

        if is_prime:
            return nextprime              # ✅ First prime found, return it
print(next_prime(7))   # → 11  
print(next_prime(13))  # → 17  
print(next_prime(50))  # → 53  

# Your task is to create a Python function called get_prime_factors(n) 
# that will return all unique prime factors of an integer n in a list. 
# A prime factor of n is a prime number that divides n without leaving a remainder. 
# The expected complexity is ((n))O(** n)).
# Note that returned prime factors should be unique and sorted in ascending order in the resulting list.

def get_prime_factors(n):
    result = []  # This list will store unique prime factors

    # Try every number i from 2 up to n (not just sqrt(n), since we don't use while)
    for i in range(2, n + 1):

        # Skip if i is not a factor of n
        if n % i != 0:
            continue  # go to next i

        # Check if i is prime
        is_prime = True  # Assume i is prime

        for j in range(2, int(i**0.5) + 1):  # Try dividing i by numbers up to √i
            if i % j == 0:
                is_prime = False  # i is not prime
                break  # stop checking this i

        if is_prime:  # if i is a prime number
            # Check if it's already in result to avoid duplicates
            already_in = False
            for k in result:
                if k == i:
                    already_in = True
                    break

            if not already_in:
                result.append(i)  # Add i to the result list

    # Now sort result manually using Bubble Sort
    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if result[j] > result[j + 1]:
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp

    return result  # Return the sorted list of unique prime factors

print(get_prime_factors(123456)) #→ [2, 3, 643] 
print(get_prime_factors(45))     #→ [3, 5]
print(get_prime_factors(84))     #→ [2, 3, 7]

# You are provided with two integers, a and b. 
# Your task is to write a Python function that checks whether both a and b are co-prime or not.
# Two numbers are said to be co-prime or mutually prime if the only positive integer
# that divides both of them is 1. The expected complexity is 
# O(max⁡(a))O(max(a,b)​
 
#  print(are_coprime(15, 28))   # Output: True
# print(are_coprime(12, 18))   # Output: False

def are_coprime(a, b):
    # Check for any common divisor from 2 up to min(a, b)
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False  # Found a common divisor, so not co-prime
    return True  # No common divisor found, so they are co-prime
print(are_coprime(15, 28))  # ✅ True
print(are_coprime(12, 18))  # ❌ False


# You are given a number n. Your task is to write a function that will return the n-th prime number. 
# The expected complexity is 
# O(n⋅n)O(n⋅n​ ).
# For example, if n is 1, the function should return 2. If n is 3, the function
#  should return the third prime number, which is 5.

def nth_prime(n: int) -> int:
    result = []  # This will store prime numbers found

    # We'll try numbers from 2 up to a large range (guaranteed to find nth prime)
    for number in range(2, 100000):  # Big enough range to reach up to 10000+ primes
        is_prime = True  # Assume current number is prime

        # Check if current number is divisible by anything before it
        for i in range(2, int(number**0.5) + 1):  # Check up to square root
            if number % i == 0:  # If divisible, it's not prime
                is_prime = False
                break  # Stop checking further

        # If it's still prime, add it to the result list
        if is_prime:
            result.append(number)

        # If we have found enough primes, return the nth one
        if len(result) == n:
            return result[-1]  # The last one added is the nth prime

    # Fallback (should never reach here if range is big enough)
    return -1

# You are given a list of n integers. Your task is to find the zero-based index of the first
# occurrence of this specific value in the list. If the provided value isn't found in the list at all, 
# return -1 instead.

# In this task, you must implement the solution without using any built-in functions or methods.
# Specifically, the use of the Python index() method of a list is not allowed in your solution.

def find_index(nums, target):
    # Loop through the list using a for loop
    for i in range(len(nums)):  # i is the index
        if nums[i] == target:   # if current value is equal to the target
            return i            # return the current index (zero-based)
    
    # If not found at all, return -1
    return -1
print(find_index([4, 7, 9, 2], 9))   # ➤ 2
print(find_index([1, 2, 3, 4], 5))   # ➤ -1
print(find_index([10, 20, 10, 30], 10))  # ➤ 0 (first occurrence)
