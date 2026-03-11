# 20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)

# ----------------------------------------------------------------------
# 1. Stack
# Push opening brackets, pop and match on closing brackets
# Time: O(n), Space: O(n)
# Best interview version — clean, efficient, handles all bracket types
# ----------------------------------------------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        opening = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char not in pairs:
                opening.append(char)
            elif not opening:
                return False
            else:
                if opening.pop() != pairs[char]:
                    return False
        return not opening

# ----------------------------------------------------------------------
# 2. Repeated String Replacement
# Remove matched pairs repeatedly until nothing changes
# Time: O(n²), Space: O(n)
# Intuitive but slow — each replace is O(n), repeated up to n/2 times
# ----------------------------------------------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        prev = None

        while s != prev:
            prev = s
            s = s.replace("()", "").replace("[]", "").replace("{}", "")

        return s == ""


############################### Use following for Practice ###############################

# ----------------------------------------------------------------------
# 1. Stack
# Time: O(n), Space: O(n)
# use a stack — push opening brackets, pop and match on closing brackets
# ----------------------------------------------------------------------

# class Solution:
#     def isValid(self, s: str) -> bool:

# ----------------------------------------------------------------------
# 2. Repeated String Replacement
# Time: O(n²), Space: O(n)
# no stack allowed — repeatedly strip matched pairs until string stops changing
# ----------------------------------------------------------------------

# class Solution:
#     def isValid(self, s: str) -> bool:
