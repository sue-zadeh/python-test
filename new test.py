# Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

# Given an array of integers numbers, your task is to check all the triples
# of its consecutive elements for being a zigzag. More formally, your task is 
# to construct an array of length numbers.length - 2, where the ith element of 
# the output array equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

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

# Return an array, where the ith element equals 1 if the triple
# (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

# [Python 3] Syntax Tips

# # Prints help message to the console
# # Returns a string
# def helloWorld(name):
#     print("This prints to the console when you Run Tests")
#     return "Hello, " + name

def solution(numbers):
 for i in range(len(numbers)):
    if numbers[i] > numbers[i] < numbers[i + 1] > numbers[i + 2]:
        return True
    if numbers[i] > numbers[i + 1] > numbers[i + 2]:
        return False
    return [i]    
# Step 1: Create an empty result string to store clean letters
# Step 2: Loop through input string
# Step 3: Keep only letters (A-Z, a-z)
# Step 4: Convert uppercase to lowercase using ASCII
# Step 5: Compare cleaned string to its reverse

def solution(s):
    result = ""  # This is our result string

    for char in s:
         # Keep letters only
        if 65 <= ord(char) <= 90:  # A-Z
            result += chr(ord(char) + 32)  # Convert to lowercase
        elif 97 <= ord(char) <= 122:  # a-z
            result += char

    # Now check if it's a palindrome
    if result == result[::-1]:  # This means reversed version of string
        return True
    else:
        return False
     
# Example 2: Capitalize first letter of each word (collecting)
# ❓ Task:
# Write a function that capitalizes the first letter of each word in a string.
# Words are separated by space.

# def solution(s):
#     result = []
#     for word in words:
#       if word== "":
#         countinue:
#         if firstletter == '':
            
            # Step 1: Create an empty result string to store clean letters
# Step 2: Loop through input string
# Step 3: Keep only letters (A-Z, a-z)
# Step 4: Convert uppercase to lowercase using ASCII
# Step 5: Compare cleaned string to its reverse
def solution(s):
    cleaned = ""  # This is our result string

    for char in s:
        ascii_code = ord(char)

        # Keep letters only
        if 65 <= ascii_code <= 90:  # A-Z
            cleaned += chr(ascii_code + 32)  # Convert to lowercase
        elif 97 <= ascii_code <= 122:  # a-z
            cleaned += char

    # Now check if it's a palindrome
    if cleaned == cleaned[::-1]:  # This means reversed version of string
        return True
    else:
        return False
# Example usage
print(solution("Was it a car or a cat I saw?"))  # Should return True
# Example usage
print(solution("Hello, World!"))  # Should return False
