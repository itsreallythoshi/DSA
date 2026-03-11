# 1. Two hashmaps
# General frequency-count solution
# Time: O(n), Space: O(n)
# use two maps - general solution - creating a frequency map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = 1 + count_s.get(char, 0)

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        
        return count_s == count_t

# 2. One hashmap, increment/decrement with early fail
# Best interview version
# Time: O(n), Space: O(n)
# one hashmap - increment and decrement - variation 1 (early fail)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = 1 + count.get(char, 0)

        for char in t:
            if char not in count:
                return False
            
            count[char] -= 1

            if count[char] < 0:
                return False
        return True

# 3. One hashmap, increment/decrement then all(...) check
# Clean compact variant
# Time: O(n), Space: O(n)
# one hashmap - increment and decrement - variation 2 - check in end. no early fail
# tighter syntax. same big-o, slightly less efficient in practice

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for char in s:
            count[char] = 1 + count.get(char, 0)

        for char in t:
            count[char] = count.get(char, 0) - 1
        return all(v == 0 for v in count.values())  


# 4. Sort both strings
# Shortest clean solution
# Time: O(n log n), Space: depends on sorting details
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
