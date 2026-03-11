# 217. Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)

# ----------------------------------------------------------------------
# 1. Brute Force
# Compare every pair of numbers
# Time: O(n²), Space: O(1)
# Simple but slow — no extra space needed
# ----------------------------------------------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

# ----------------------------------------------------------------------
# 2. HashSet with Early Return
# Track seen numbers, return True on first duplicate
# Time: O(n), Space: O(n)
# Best interview version — one pass, exits as soon as duplicate is found
# ----------------------------------------------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

# ----------------------------------------------------------------------
# 3. Set Dedup One-Liner
# Compare original length to deduplicated length
# Time: O(n), Space: O(n)
# Cleanest syntax — if set is smaller, a duplicate was removed
# ----------------------------------------------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# ----------------------------------------------------------------------
# 4. Sort then Compare Neighbors
# Sort, then check if any adjacent elements are equal
# Time: O(n log n), Space: O(1) in-place / O(n) if sort copies
# No extra set — duplicates become adjacent after sorting
# ----------------------------------------------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False

