# 167. Two Sum II - Input Array Is Sorted (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

# ----------------------------------------------------------------------
# 1. Two Pointers
# Shrink window from both ends using sorted order
# Time: O(n), Space: O(1)
# Best solution — exploits sorted property, no extra space needed
# ----------------------------------------------------------------------

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            curr = numbers[i] + numbers[j]
            if curr == target:
                return [i + 1, j + 1]
            elif curr < target:
                i += 1
            else:
                j -= 1

# ----------------------------------------------------------------------
# 2. Binary Search
# For each element, binary search for its complement in the rest of the array
# Time: O(n log n), Space: O(1)
# Challenge approach — still no extra space, but less optimal than two pointers
# ----------------------------------------------------------------------

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            complement = target - numbers[i]
            left, right = i + 1, n - 1

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    left = mid + 1
                else:
                    right = mid - 1