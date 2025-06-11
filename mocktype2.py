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

print(binary_search([1, 3, 5, 7, 9], 5))  # ✅ Output: 2



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
