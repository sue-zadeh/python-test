
# ✅ Task 3: Binary Tree Level Order Traversal
# 🧠 Type: 3️⃣ Breadth-First Traversal (Queue)
# ❓ What it does:
# It prints all nodes of a binary tree level by level from top to bottom.

# ✅ Example:
# For this tree:

#        1
#      /   \
#     2     3
#    / \     \
#   4   5     6

# Output: [1, 2, 3, 4, 5, 6]

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
    result = []
    queue = []

    if root:
        queue.append(root)

    while queue:
        current = queue[0]
        queue = queue[1:]

        result.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# Build the example tree:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(level_order(root))  # ✅ Output: [1, 2, 3, 4, 5, 6]


# ✅ Task – First Unique Character Index
# Type: 3️⃣ – String + Index Logic
# Difficulty: Medium
# No built-in functions like .count(), .index(), dict, set, or collections.

# 🧩 Description:
# Given a string s, return the index of the first non-repeating character.
# If every character repeats, return -1.

# 📥 Input:
# A string s (1 ≤ length ≤ 1000), only lowercase letters.

# 📤 Output:
# An integer: index of the first unique character, or -1 if none.
                    
#  s = "leetcode"
# Output: 0  # 'l' appears only once, first
def solution(s):
    # For each character in the string
    for i in range(len(s)):
        is_unique = True  # Assume it's unique

        # Check every other character
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                is_unique = False
                break  # Not unique, no need to check more

        # If still unique, return this index
        if is_unique:
            return i

    # If no unique character found
    return -1

print(solution("leetcode"))  # Output: 0 ('l' is unique)
print(solution("aabb"))      # Output: -1 (no unique letter)

# ✅ Task – Count Letters and Digits
# Type: 3️⃣ – String Parsing
# Difficulty: Easy-Medium

# 🧩 Description:
# You are given a string s.
# Return a list with two numbers:

# The number of letters in the string (a–z, A–Z)

# The number of digits in the string (0–9)

# 📥 Input:
# A string s (length ≤ 1000)

# 📤 Output:
# A list of two integers: [letter_count, digit_count]

# 📘 Example:
# python
# Copy
# Edit
# s = "abc123xyz9"
# Output: [6, 4]  # 6 letters: a, b, c, x, y, z; 4 digits: 1, 2, 3, 9
# ❗ Constraints:
# Do not use built-in functions like isalpha(), isdigit(), or re (regex).

# You must use only for loops and check using character codes (ord()).


     