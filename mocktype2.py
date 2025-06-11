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

# ✅ Task – Merge Intervals
# Type 2 or Type 3 depending on how deep it goes.
# 🧠 You're given a list of intervals like:

# [[1, 3], [2, 4], [6, 8]]
# Goal: Merge overlapping ones.
def merge_intervals(intervals):
    # Step 1: Sort intervals based on the start time
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i][0] > intervals[j][0]:
                intervals[i], intervals[j] = intervals[j], intervals[i]

    merged = [intervals[0]]  # Start with the first interval

    for i in range(1, len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]
        last_end = merged[-1][1]

        # If current start is less than or equal to last merged end, merge
        if start <= last_end:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append(intervals[i])  # No overlap, add new interval

    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # ✅

# Task 2: Binary Search
# 🧠 Type: 2️⃣ – Classic sorted array search
# 📘 Goal: Find the index of a target in a sorted array.

# 📝 Example:
# Input: nums = [1, 3, 5, 7, 9], target = 5
# Output: 2
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
