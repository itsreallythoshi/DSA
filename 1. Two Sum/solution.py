# 1. Two Sum (https://leetcode.com/problems/two-sum/)

# ----------------------------------------------------------------------
# 1. Brute Force
# Try every pair of numbers
# Time: O(n²), Space: O(1)
# Simple but slow — nested loop checks every combination
# ----------------------------------------------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# ----------------------------------------------------------------------
# 2. Hash Map
# Store seen numbers and look up the complement
# Time: O(n), Space: O(n)
# Best standard solution — one pass, check if complement was seen before
# ----------------------------------------------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# ----------------------------------------------------------------------
# 3. Sort + Two Pointers
# Preserve original indices, sort by value, use two pointers
# Time: O(n log n), Space: O(n)
# Useful pattern — must preserve original indices before sorting
# ----------------------------------------------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()

        left, right = 0, len(arr) - 1

        while left < right:
            curr = arr[left][0] + arr[right][0]

            if curr == target:
                return [arr[left][1], arr[right][1]]
            elif curr < target:
                left += 1
            else:
                right -= 1


############################### Use following for Practice ###############################

# ----------------------------------------------------------------------
# 1. Brute Force
# Time: O(n²), Space: O(1)
# try every pair — nested loop, no extra space
# ----------------------------------------------------------------------

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

# ----------------------------------------------------------------------
# 2. Hash Map
# Time: O(n), Space: O(n)
# one pass with a hashmap — store seen numbers, look up the complement
# ----------------------------------------------------------------------

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

# ----------------------------------------------------------------------
# 3. Sort + Two Pointers
# Time: O(n log n), Space: O(n)
# sort + two pointers — preserve original indices before sorting
# ----------------------------------------------------------------------

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
