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