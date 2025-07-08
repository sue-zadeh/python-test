// ✅ Task 1 — Memory Allocation Simulation
// You are given a memory represented by a list of integers where 0 means a free slot. You receive a list of queries, each of which is either:

// [0, size]: allocate size consecutive free memory slots starting from a multiple of 8. If successful, mark those slots with a unique ID and return the starting index. If not possible, return -1.

// [1, id]: free all memory blocks marked with id. Return the number of blocks freed, or -1 if none found.

// ✅ Task 2 — Magical Digit Swap
// In a land where numbers hold magical powers, a gemstone can transform one number into another by swapping at most two of its digits.
// Your task:
// Given an array of numbers, count how many distinct pairs (i, j) exist where 0 ≤ i < j < numbers.length and one number can be transformed into the other via at most two digit swaps.
// ✨ Note: Equal numbers (without any swap) should also be considered as valid magical pairs.

// ✅ Task 3 — Zigzag Triples
// A zigzag triple in an array is a group of 3 elements such that either:

// a < b > c or

// a > b < c
// Your task is to count the number of such zigzag triples in the array.
// Example: For input [1, 3, 2, 4], the zigzag triples are: (1,3,2), (3,2,4) → output is 2.

// ✅ Task 4 — String Merge and Balance
// Given a string, check whether it's possible to remove at most one character to make it a balanced string.
// A balanced string is one where all characters appear the same number of times.
// Example:

// Input: "aabbcc" → Already balanced → Return true

// Input: "aabbc" → Remove one 'c' → becomes "aabb" → Return true

// Input: "aabbcd" → Can't balance by removing one character → Return false