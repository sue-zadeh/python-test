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