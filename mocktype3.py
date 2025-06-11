
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
