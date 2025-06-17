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
        for i in range(10):                # loop from i = 0 to 9
            if number >= 10 ** i:          # if number is bigger than or equal to 10^i
                count = i + 1              # then the digit count is i + 1
        if number == 0:                    # special case: if number is zero
            count = 1                      # set count to 1 (because 0 has 1 digit)
        result.append(count)               # add the count to result list
    return result                          # return the final result list

# Example use
print(solution([5, 23, 100, -9]))          # Output: [1, 2, 3, 1]
