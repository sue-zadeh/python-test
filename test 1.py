# Description:
# Given an integer n, your task is to create a square frame of size n,
#  represented as an array of strings.
# The frame should consist of empty space, enclosed by lines made of * characters
#  as follows:
# For n = 8, the output should be:
# [
#   "********",
#   "*      *",
#   "*      *",
#   "*      *",
#   "*      *",
#   "*      *",
#   "*      *",
#   "********"
# ]
# For n = 5:
# [
#   "*****",
#   "*   *",
#   "*   *",
#   "*   *",
#   "*****"
# ]
# For n = 2:
# [
#   "**",
#   "**"
# ]


def solution(n):
    # Create an empty list that will hold each row of the frame
    result = []

    # Loop over each row index from 0 to n-1
    for i in range(n):
        line = ""  # Start with an empty line for this row

        # Loop over each column index from 0 to n-1
        for j in range(n):
            # First or last row → fill all with "*"
            if i == 0 or i == n - 1:
                line = line + "*"
            # First or last column in middle rows → put "*"
            elif j == 0 or j == n - 1:
                line = line + "*"
            # Inner cells → fill with space
            else:
                line = line + " "

        # After building the row, add it to the result list
        result.append(line)

    # Return the final list of strings representing the frame
    return result

# 🧪 How to test it:
# Test 1
output = solution(5)
for row in output:
    print(row)

# Test 2
print("----")
output = solution(2)
for row in output:
    print(row)

# Test 3
print("----")
output = solution(8)
for row in output:
    print(row)

    #=================================
    #=================================

# Add every i-th digit from the end of both strings.
# If one string is shorter, use the digit from the longer string.
# Return the string of those sums (each sum becomes a number in the result).


# ✅ Task 2: Sum of Digit Strings from End
# 📄 Description:
# You are given two numerical strings, and your task is to return
#  the sum of their digits, as described below:
# Add every i-th digit of the first string to the i-th digit of the second string,
#  both counted from the end.
# If the i-th digit of one of the strings is missing (shorter length), 
# use the digit of the other string as-is.
# Return a string of those sums concatenated with each other.

# 📌 Example:
# For a = "99" and b = "99",
# → output: "1818"
# (Both digits are 9 + 9 = 18)

# For a = "11" and b = "9",
# → output: "110"
# (1 + nothing = 1, 1 + 9 = 10 → becomes "110")

# ⚠️ Constraints:
# Input: a and b are digit-only strings (no leading zeroes)
# Output: a string formed by concatenating digit sums (not total sum)
# Length of input strings ≤ 10⁵
# Time limit: 4 seconds

def solution(a, b):
    # Step 1: Convert string a into a list of digits
    a_digits = []  
    for i in range(len(a)):    
    #in a ord("0") is 48, so this subtracts 48 to convert character to digit
        a_digits = a_digits + ord(a[i]) - ord("0")   # add digit to list

    # Step 2: Convert string b into a list of digits
    b_digits = [] 
    for i in range(len(b)):  
        b_digits = b_digits + ord(b[i]) - ord("0")  # add digit to list

    # Step 3: Get the longer length between the two digit lists
    if len(a_digits) > len(b_digits):
        max_len = len(a_digits)
    else:
        max_len = len(b_digits)
    # Step 4: Initialize result string to store the final answer (in reverse order)
    result = []

    # Loop from the end (right to left) of both lists
    for i in range(1, max_len + 1):  # loop i = 1 to max_len
        digita = 0
        digitb = 0

        if len(a_digits) - i >= 0:
            digita = a_digits[len(a_digits) - i]

        if len(b_digits) - i >= 0:
            digitb = b_digits[len(b_digits) - i]

        total = digita + digitb

        if total >= 10:
            result = result + [chr(ord("0") + (total // 10))]
            result = result + [chr(ord("0") + (total % 10))]
        else:
            result = result + [chr(ord("0") + total)]
       # Step 5: Reverse the result
    final = ""
    for i in range(len(result) - 1, -1, -1):
        final = final + result[i]

    return final


print(solution("99", "99"))     # Expected: "1818"
print(solution("11", "9"))      # Expected: "110"
print(solution("123", "5"))     # Expected: "128"
print(solution("5", "99999"))   # Expected: "99994"
print(solution("1111", "1111")) # Expected: "2222"




  





# ✅ Task 3: Memory Manager with Allocation & Erase
# 📄 Description:
# You are given an array of integers memory consisting of 0s and 1s:
# memory[i] = 0 → the i-th memory unit is free
# memory[i] = 1 → the i-th memory unit is occupied
# The memory is aligned with segments of 8 units — so all allocated memory blocks
#  must start at an index divisible by 8 (e.g. 0, 8, 16…).
# 💡 Your task is to perform 2 types of queries:
# 🔹 alloc x:
# Find the leftmost aligned block (start index divisible by 8) with x consecutive
#  free units
# Replace them with the same allocation ID
# This ID starts at 1 and increases with each successful allocation
# If no suitable block is found, return -1
# Otherwise, return the start index of the allocated block

# 🔹 erase ID:
# If a block exists with valsum_digit = 0  # this will hold the sum of current digitsue = ID, erase it (replace all its values with 0)
# Return the number of cells erased
# If no such block exists or it’s already deleted, return -1

# 🧾 Notes:
# The ID is automatically generated using an atomic counter (starts at 1)
# x can be bigger than 8, so the block may span more than one segment
# 🔢 Input Format:
# queries is an array of [2]-element arrays
# If queries[i][0] == 0, it's an alloc query and queries[i][1] is x
# If queries[i][0] == 1, it's an erase query and queries[i][1] is ID




