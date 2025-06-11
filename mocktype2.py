# Best structure for camelCase splitter:
# ✅ Version using ord() — your style — with full comments:
def can_split_camel_case(words, camelCase):
    result = []  # to store split words
    word = ""    # temporary word collector

    for char in camelCase:
        # If uppercase letter found (ASCII 65–90)
        if 65 <= ord(char) <= 90:
            # if word already collected, push it to result
            if word:
                result.append(word)
            # start new word by converting to lowercase (ASCII trick)
            word = chr(ord(char) + 32)
        else:
            # just add lowercase char to current word
            word += char

    # add last collected word
    if word:
        result.append(word)

    # check if every word is in the given list
    for w in result:  # result contains the words we split from the camelCase string
      if w not in words:  # if any of them is not in the known words list
        return False
    return True  # all of them were in the list, so it’s valid

example_words = ["apple", "banana", "orange"]
print(can_split_camel_case(example_words, "appleBanana"))  # ✅ True
print(can_split_camel_case(example_words, "appleOrange"))  # ✅ True
print(can_split_camel_case(example_words, "appleWater"))   # ❌ False

# # ✅ Task: Merge Intervals
# 🧠 Type: 2️⃣ Sorting & Searching
# 🧪 Also Seen In: Visa coding tests
# 📘 Full Task Description:

# You're given a list of intervals, where each interval is a pair of numbers:
#  the start and end of a time range (or segment).
# If any intervals overlap, your goal is to merge them into one continuous interval.
# Input:  [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# ❓ Why:
# [1, 3] and [2, 6] overlap, so we merge them into [1, 6].
# [8, 10] and [15, 18] don’t overlap with others — they stay as they are.

def merge_intervals(intervals):
    # Step 1: Sort the intervals by their start time using nested loops
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i][0] > intervals[j][0]:
                # Swap to sort based on starting value
                intervals[i], intervals[j] = intervals[j], intervals[i]

    merged = [intervals[0]]  # Start with the first interval as initial merged one

    # Step 2: Go through each interval and merge if they overlap
    for i in range(1, len(intervals)):
        start = intervals[i][0]       # current interval's start
        end = intervals[i][1]         # current interval's end
        last_end = merged[-1][1]      # end of the last merged interval

        if start <= last_end:
            # Merge: update the end of last interval if overlapping
            if end > last_end:
                merged[-1][1] = end
        else:
            # No overlap: just add the interval
            merged.append(intervals[i])

    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # ✅ Output: [[1, 6], [8, 10], [15, 18]]

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # ✅

# Task 2: Binary Search
# 🧠 Type: 2️⃣ – Classic sorted array search
# 📘 Goal: Find the index of a target in a sorted array.
# 🔍 Task:
# Given a sorted list of numbers and a target number, find the index of that target using binary search.
# 📝 Example:
# Input: nums = [1, 3, 5, 7, 9], target = 5
# Output: 2
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    # Loop enough times to cover the search space
    for _ in range(len(nums)):
        if left > right:
            break  # stop if range is invalid

        mid = (left + right) // 2  # calculate middle

        if nums[mid] == target:
            return mid  # found!
        elif nums[mid] < target:
            left = mid + 1  # search right half
        else:
            right = mid - 1  # search left half

    return -1  # not found

print(binary_search([1, 3, 5, 7, 9], 9))  # ✅ Output: 3



#*****************************************
# ✅ Task 3: Quicksort (Sort an Array)
# 🧠 Type: 2️⃣ – Sorting Algorithm
# 📘 Goal: Sort an array using quicksort.

# ✅ Code with comments:
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # First element as pivot
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([3, 6, 2, 8, 4, 1]))  # Output: [1, 2, 3, 4, 6, 8]

# 🔷 Task 3 – Longest Substring Without Repeating Characters
# Type: 2️⃣ – Sliding Window (String + Hashing)
# You’re given a string, and you have to find the longest
# part of the string where no characters are repeated.
# A substring is a continuous sequence of characters.
# You cannot skip characters.
# You must return the length of the longest such substring.
# 🔍 Example:
# Input: "abcabcbb"
# → Let's walk through substrings:

# "abc" ✅ (no repeat, length 3)
# "abca" ❌ (repeats 'a')
# "bca" ✅ (still 3)
# So the answer is:
# 3 → because "abc" is the longest substring without repeating characters.

# Goal: Find the length of the longest substring with all unique characters.
def longest_unique_substring(s):
    max_len = 0                    # Track maximum length
    start = 0                      # Start of current unique substring
    seen = []                      # Track characters in current window

    for i in range(len(s)):        # Go through each character by index
        repeated = False           # Check if current char was seen before

        # Manually check for repetition using a for loop
        for j in range(len(seen)):
            if s[i] == seen[j]:    # If current char exists in seen list
                repeated = True    # Mark as repeated
                # Move start to 1 past the previous same character
                start += j + 1     # Skip everything before and including repeated char
                break              # Exit the loop as we found duplicate

        # Rebuild seen list from new start
        seen = []                  # Clear and rebuild
        for k in range(start, i + 1):
            seen.append(s[k])      # Rebuild the list from start to i

        # Update maximum length if longer window found
        if len(seen) > max_len:
            max_len = len(seen)

    return max_len

# ✅ Test cases
print(longest_unique_substring("abcabcbb"))  # Output: 3 ("abc")
print(longest_unique_substring("bbbbb"))     # Output: 1 ("b")
print(longest_unique_substring("pwwkew"))    # Output: 3 ("wke")

#  Task: Shortest Path in an Unweighted Graph
# Type: Type 2️⃣ – Sorting & Searching
# Concept: Use Breadth-First Search (BFS) to find the shortest path from a start node
# to all other nodes in an unweighted graph.
# 🧠 What’s the task?
# You're given a graph like this:

# graph = {
#   'A': ['B', 'C'],
#   'B': ['A', 'D', 'E'],
#   'C': ['A', 'F'],
#   'D': ['B'],
#   'E': ['B', 'F'],
#   'F': ['C', 'E']
# }

def shortest_path_unweighted(graph, start):
    # Step 1: Create a dictionary to store distances
    distance = {}
    for node in graph:
        distance[node] = -1  # -1 means not visited

    distance[start] = 0  # Distance to itself is 0

    # Step 2: BFS Queue: we use a list to simulate a queue
    queue = [start]  # Start BFS from the start node

    for index in range(len(queue)):  # Simulate queue with for loop
        current = queue[index]  # Current node being processed

        for i in range(len(graph[current])):  # Loop through neighbors
            neighbor = graph[current][i]
            if distance[neighbor] == -1:  # If not visited
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)  # Add neighbor to queue

    return distance  # Return distances to all nodes
graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'F'],
  'D': ['B'],
  'E': ['B', 'F'],
  'F': ['C', 'E']
}

print(shortest_path_unweighted(graph, 'A'))
# Expected:
# {
#   'A': 0,
#   'B': 1,
#   'C': 1,
#   'D': 2,
#   'E': 2,
#   'F': 2
# }
#  Task 1: Number of Islands (DFS style using stack)
# Type: 2️⃣ Graph / DFS
# Goal: Count how many separate islands (groups of 1s) exist in a grid (matrix). 
# An island is connected vertically or horizontally.

def num_islands(grid):
    rows = len(grid)           # Number of rows
    cols = len(grid[0])        # Number of columns
    count = 0                  # Total islands found
    visited = []               # To track visited cells

    # Create a visited grid of same size filled with False
    for i in range(rows):
        visited.append([False] * cols)

    # Loop through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find a '1' and not visited
            if grid[r][c] == '1' and not visited[r][c]:
                count += 1           # Found a new island
                stack = [[r, c]]     # Start DFS using a stack

                for i in range(len(stack)):
                    row, col = stack[i][0], stack[i][1]
                    visited[row][col] = True

                    # Check 4 directions
                    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                    for d in range(len(directions)):
                        new_row = row + directions[d][0]
                        new_col = col + directions[d][1]

                        # Make sure new cell is inside grid and is '1' and not visited
                        if (0 <= new_row < rows and 0 <= new_col < cols and
                            grid[new_row][new_col] == '1' and not visited[new_row][new_col]):
                            stack.append([new_row, new_col])  # Add to stack
    return count

# Example:
grid = [
    ["1","1","0","0"],
    ["1","0","0","1"],
    ["0","0","1","1"]
]
print(num_islands(grid))  # Output: 3

# ✅ Task 2: Subset Sum Problem
# Type: 2️⃣ Dynamic Programming
# Goal: Return True if there exists a subset whose sum equals a target value.
def subset_sum(arr, target):
    n = len(arr)
    dp = []

    # Create DP table of size (n+1) x (target+1)
    for i in range(n + 1):
        row = []
        for j in range(target + 1):
            if j == 0:
                row.append(True)  # Sum 0 is always possible
            elif i == 0:
                row.append(False)  # If array is empty and sum > 0, it's False
            else:
                row.append(False)
        dp.append(row)

    # Fill the DP table
    for i in range(1, n + 1):  # Loop through items
        for j in range(1, target + 1):  # Loop through all possible sums
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]  # Don't include this number
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]  # Include or exclude
    return dp[n][target]

# Example:
print(subset_sum([3, 34, 4, 12, 5, 2], 9))  # Output: True (4+5)

# ✅ Task 3: Longest Common Subsequence
# Type: 2️⃣ Dynamic Programming
# Goal: Find the longest subsequence (not necessarily continuous) that exists in both strings.
def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create 2D DP table (m+1) x (n+1)
    dp = []
    for i in range(m + 1):
        row = []
        for j in range(n + 1):
            row.append(0)
        dp.append(row)

    # Fill the table
    for i in range(1, m + 1):  # Loop through s1
        for j in range(1, n + 1):  # Loop through s2
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # Match found
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # No match

    return dp[m][n]  # The last cell has the LCS length

# Example:
print(longest_common_subsequence("abcde", "ace"))  # Output: 3 ("ace")

#********************************
# ✅ Task – Shift Letters by 2 Positions
# Type: 2️⃣ – Medium String Manipulation (CodeSignal style)
# Goal: Given a string, shift every letter 2 places forward in the alphabet.

# Wrap around from 'z' to 'b' and 'Z' to 'B'.

# Keep digits and symbols unchanged.

# Example:
# Input: "abcXYZz!"
# → Output: "cdeZABb!"
def shift_letters(s):
    result = ""  # to store the final shifted string

    for char in s:
        if 'a' <= char <= 'z':  # if it's a lowercase letter
            # shift by 2 and wrap using modulo 26
            new_char = chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
            result += new_char
        elif 'A' <= char <= 'Z':  # if it's an uppercase letter
            new_char = chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
            result += new_char
        else:
            # keep digits and special characters unchanged
            result += char

    return result

# 🔹 Test it
print(shift_letters("abcXYZz!"))  # ✅ Output: "cdeZABb!"

