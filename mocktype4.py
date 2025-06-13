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

# Task: sumDivisibleByK
# You're given:

# an array a of integers

# a number k

# Your goal:
# 👉 Count the number of unique index pairs i < j where
#   (a[i] + a[j]) % k == 0
def solution(a, k):
    result = []  # to collect valid pairs
    count = 0   # to count valid pairs
    # loop through all index pairs (i, j) where i < j
    for i in range(len(a)):
        for j in range(i + 1, len(a)):  # ensures i < j
            # check if the sum of a[i] and a[j] is divisible by k
            if (a[i] + a[j]) % k == 0:
                result.append((a[i], a[j]))  # save the pair
                count += 1

    return (result, count)  
# Example usage:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(solution(a, k))  # Output: ([(1, 2), (1, 5), (2, 4), (3, 6), (4, 5), (6, 9), (7, 8)], 7)

# ✅ Task 4: Find the Shortest Path in a Graph (Dijkstra’s Algorithm)
# 🧠 Type: 4️⃣ Graph / Dynamic Programming / Greedy
# This is an advanced Type 4 question from Visa-level tests.

# 🔍 Goal:
# Find the shortest path from one node to all others in a weighted graph.
import heapq  # for priority queue

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # distance to self is 0
    queue = [(0, start)]  # (distance, node)

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue  # already found a shorter way

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example graph:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))  # ✅ Shortest distances from 'A'

#  Task: Rotten Oranges – Spread of rot in a grid
# Type: Type 4️⃣ – Simulation with matrix & multiple queues
# Goal:
# Given a 2D grid where:

# 0 = empty cell

# 1 = fresh orange

# 2 = rotten orange

# Each minute, a rotten orange turns all its adjacent (up/down/left/right) fresh oranges rotten.
# Return the minimum number of minutes to rot all oranges. Return -1 if impossible.

def oranges_rotting(grid):
    rows = len(grid)           # Number of rows
    cols = len(grid[0])        # Number of columns
    fresh = 0                  # Counter for fresh oranges
    rotten = []                # List of coordinates with rotten oranges

    # Step 1: Count fresh oranges and store initial rotten positions
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:        # Fresh orange
                fresh += 1
            elif grid[i][j] == 2:      # Rotten orange
                rotten.append((i, j))

    # If no fresh oranges to begin with
    if fresh == 0:
        return 0

    time = 0  # Minutes passed

    # Directions: up, down, left, right
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # Loop while we still have rotten oranges to process
    for minute in range(10000):  # simulate max 10,000 minutes
        new_rotten = []  # List to store newly rotted oranges this minute

        for k in range(len(rotten)):
            i, j = rotten[k]  # Get current rotten orange

            for d in range(len(directions)):
                di, dj = directions[d]   # Direction to check
                ni = i + di              # New row index
                nj = j + dj              # New col index

                # Check if inside grid and fresh
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    grid[ni][nj] = 2     # Make it rotten
                    fresh -= 1           # Reduce fresh count
                    new_rotten.append((ni, nj))  # Add to next round

        if len(new_rotten) == 0:
            break  # No more rot to spread

        rotten = new_rotten  # Prepare for next minute
        time += 1            # Increment time

    # After loop, check if any fresh orange remains
    if fresh == 0:
        return time
    else:
        return -1
# 11.	Sudoku Solver – Solve a partially filled Sudoku grid.

def is_valid(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            # Find empty cell
            if board[row][col] == 0:
                # Try digits 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        # Recursive call using manual for-loop style
                        solved = solve_sudoku(board)
                        if solved:
                            return True

                        # Undo if it didn't work
                        board[row][col] = 0

                # No number fits, so return False
                return False

    # All cells are filled
    return True

# Example board (0 means empty cell)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve_sudoku(sudoku_board)

# Print solved board
for row in sudoku_board:
    print(row)

# ✅ Task – Count Matching Pairs
# Type: 4️⃣ – Logic / Counting / Hashmap style (no built-ins)
# Difficulty: Medium to Hard (CodeSignal real exam style)
# 🧩 Description:
# You are given an array of integers.
# Your task is to return the number of pairs (i, j) such that:
# i < j
# numbers[i] == numbers[j]

# Do not use built-in methods like count(), set(), dict(), or collections.
# You must use for loops only and basic lists.

# 🔢 Input:
# A list of integers numbers (length ≤ 1000, values: 0 ≤ number ≤ 1000)
def solution(nums):
    # result =[]
    count = 0
    # count_min = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
           if nums[i] == nums[j]:
             count += 1
    return (count)   
print(solution([1, 2, 1, 2, 1]))  


# ✅ Task – Unique Sum to Zero
# Type: 4️⃣ – Math + Logic
# Difficulty: Easy-Medium
# No built-in methods (like set() or sum()) allowed. Use only for loops and basic operations.
# 🧩 Description:
# You are given an integer n.
# Return an array of n unique integers such that their sum is 0.
# 📥 Input:
# An integer n (1 ≤ n ≤ 1000)
# 📤 Output:
# A list of n integers, all unique, and their sum must equal 0.
# ⚠️ Constraints:
# You can only use for loops and math.
# Don’t use built-in Python functions like sum(), set() or list comprehensions.
# 🧠 Hint:
# Use pairs like [-1, 1], [-2, 2], etc.
# If n is odd, include a 0 too.
# 📘 Example 1:
# n = 4
# Output: [-2, -1, 1, 2]  # or any variation with unique numbers summing to 0
# 📘 Example 2:
# n = 5
# Output: [-2, -1, 0, 1, 2]
def solution(n):
    result = []

    # Add pairs like [-1, 1], [-2, 2], ...
    for i in range(1, n // 2 + 1):
        result.append(-i)
        result.append(i)

    # If n is odd, also add 0
    if n % 2 != 0:
        result.append(0)

    return result
print(solution(5))  # Output: [-1, 1, -2, 2, 0]
print(solution(4))  # Output: [-1, 1, -2, 2]

#    Given an integer n, return a square frame (as a list of strings)
# of size n made of * characters around the border and spaces inside.

def solution(n):
    result = []  # Create an empty list to store each line

    for i in range(n):  # Outer loop for each row
        line = ""  # Start with an empty string for the current row

        for j in range(n):  # Inner loop for each column
            if i == 0 or i == n - 1:  # First or last row
                line = line + "*"
            elif j == 0 or j == n - 1:  # First or last column
                line = line + "*"
            else:  # Middle of the frame
                line = line + " "

        result.append(line)  # Add the full line to the result

    return result  # Return the list of lines

               
 #  Output for n = 7:
#  *******
# *     *
# *     *
# *     *
# *     *
# *     *
# *******

output = solution(6)
for row in output:
    print(row)

# Add every i-th digit from the end of both strings.
# If one string is shorter, use the digit from the longer string.
# Return the string of those sums (each sum becomes a number in the result).

# 💡 Logic Summary:
# Converts string to digit array without int() or list()

# Adds digits from the right side (like a manual column sum)

# Handles different lengths

# Reverses final string without [::-1]

def solution(a, b):
    # Convert input strings to digit arrays manually
    a_digits = []
    for i in range(0, len(a)):
        a_digits = a_digits + [ord(a[i]) - ord('0')]  # convert char to digit

    b_digits = []
    for i in range(0, len(b)):
        b_digits = b_digits + [ord(b[i]) - ord('0')]

    # Find the maximum length of the result
    max_len = len(a_digits)
    if len(b_digits) > max_len:
        max_len = len(b_digits)

    result = ""  # Final result string

    # Loop from the end to the beginning
    for i in range(1, max_len + 1):
        sum_digit = 0

        # Add from a if available
        if len(a_digits) - i >= 0:
            sum_digit = sum_digit + a_digits[len(a_digits) - i]

        # Add from b if available
        if len(b_digits) - i >= 0:
            sum_digit = sum_digit + b_digits[len(b_digits) - i]

        # Convert sum_digit to characters (2 digits handled) and add to result
        if sum_digit >= 10:
            d1 = sum_digit // 10
            d2 = sum_digit % 10
            result = result + chr(ord('0') + d1)
            result = result + chr(ord('0') + d2)
        else:
            result = result + chr(ord('0') + sum_digit)

    # Reverse the result manually
    final_result = ""
    for i in range(len(result) - 1, -1, -1):
        final_result = final_result + result[i]

    return final_result

print(solution("99", "99"))     # Expected: "1818"
print(solution("11", "9"))      # Expected: "110"
print(solution("123", "5"))     # Expected: "128"
print(solution("1000", "1000")) # Expected: "20000"


#Examples:
# ord("0")       → 48
# ord("1")       → 49
# ord("9")       → 57
# chr(48 + 3)    → "3"
# chr(48 + 10)   → ":" ❌ (not a digit)


#  Problem Summary:
# You are given:

# A memory array of 0s and 1s

# 0 = free memory

# 1 = used memory

# You also receive a list of queries:

# Each query is one of two types:

# alloc x: allocate x consecutive 0s starting at a start index divisible by 8

# erase id: remove a previously allocated block with a given ID and turn them back to 0

