# 4. Task for Frequency (Type 4)
# ✅ Type 4: Advanced Logic / Grouping Task

# ❓ Task:
# You are given a list of integers. Return the number that appears most frequently in the list.
# If there is a tie, return the smallest such number.
# Don’t use collections.Counter() or dict (CodeSignal rules).
# Use only basic loops and arrays.

# Step-by-step Plan:
# Create two arrays:

# values = [] to store unique numbers
# counts = [] to store how many times each value appeared
# Loop through nums:
# If number is not in values, add it and set count to 1
# If it exists, increment its count in counts
# Find the highest frequency and return the smallest value that has that frequency

# Quick Recap of Logic:
# We're simulating a dictionary using two lists: values and counts.

# Then we find the highest count in counts.

# If there's a tie, we choose the smallest number with that frequency.

def most_frequent(nums):
    values = []     # List to store unique values we see
    counts = []     # Parallel list to track how many times each value appears

    for i in range(len(nums)):   # Go through each number in input
        found = False            # Flag to check if we’ve seen this number before

        for j in range(len(values)):  # Loop through stored unique values
            if nums[i] == values[j]:  # If current number is already stored
                counts[j] += 1        # Increase its count
                found = True          # Mark as found
                break                 # No need to check more

        if not found:               # If number is new
            values.append(nums[i])  # Add it to the unique values list
            counts.append(1)        # Start its count at 1

    max_count = counts[0]        # Start assuming first value is the most frequent
    min_val = values[0]          # And that value is the result (so far)

    for i in range(1, len(values)):     # Go through the rest of the unique values
        if counts[i] > max_count:       # Found a new higher frequency
            max_count = counts[i]       # Update highest frequency
            min_val = values[i]         # Update the value to return
        elif counts[i] == max_count and values[i] < min_val:
            # If tie in frequency but value is smaller, choose the smaller one
            min_val = values[i]

    return min_val    # Final answer: most frequent (smallest if tie)

most_frequent([4, 2, 2, 3, 3, 3, 1, 1, 1]) # # 3
most_frequent([1, 2, 3, 4, 5]) # # 1 (all unique)
most_frequent([10, 20, 10, 20, 30]) # # Tie: return smaller

#==========================================
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
