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


############################### Use following for Practice ###############################

# ----------------------------------------------------------------------
# 1. Brute Force
# Time: O(n²), Space: O(1)
# try every pair — nested loop, no extra space allowed
# ----------------------------------------------------------------------

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:

# ----------------------------------------------------------------------
# 2. HashSet with Early Return
# Time: O(n), Space: O(n)
# use a set — return True the moment you see a number you've already seen
# ----------------------------------------------------------------------

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:

# ----------------------------------------------------------------------
# 3. Set Dedup One-Liner
# Time: O(n), Space: O(n)
# solve in one line — compare lengths before and after deduplication
# ----------------------------------------------------------------------

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:

# ----------------------------------------------------------------------
# 4. Sort then Compare Neighbors
# Time: O(n log n), Space: O(1)
# no set allowed — sort first, then find duplicates by comparing neighbors
# ----------------------------------------------------------------------

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
