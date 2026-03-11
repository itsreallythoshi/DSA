// 1. Two Sum (https://leetcode.com/problems/two-sum/)

// ----------------------------------------------------------------------
// 1. Brute Force
// Try every pair of numbers
// Time: O(n²), Space: O(1)
// Simple but slow — nested loop checks every combination
// ----------------------------------------------------------------------

var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
};

// ----------------------------------------------------------------------
// 2. Hash Map
// Store seen numbers and look up the complement
// Time: O(n), Space: O(n)
// Best standard solution — one pass, check if complement was seen before
// ----------------------------------------------------------------------

var twoSum = function(nums, target) {
    const seen = new Map();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }

        seen.set(nums[i], i);
    }
};

// ----------------------------------------------------------------------
// 3. Sort + Two Pointers (broken version — shows the pitfall)
// Two pointers on unsorted array, without preserving original indices
// Time: O(n log n), Space: O(1)
// Broken — sorting loses original indices, so returned indices are wrong
// ----------------------------------------------------------------------

var twoSum = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    nums.sort((a, b) => a - b);

    while (left < right) {
        const sum = nums[left] + nums[right];

        if (sum === target) {
            return [left, right];  // wrong — these are sorted positions, not original indices
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
};

// ----------------------------------------------------------------------
// 3. Sort + Two Pointers (correct version)
// Preserve original indices, sort by value, use two pointers
// Time: O(n log n), Space: O(n)
// Useful pattern — must preserve original indices before sorting
// ----------------------------------------------------------------------

var twoSum = function(nums, target) {
    const arr = nums.map((value, index) => ({ value, index }));

    arr.sort((a, b) => a.value - b.value);

    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        const sum = arr[left].value + arr[right].value;

        if (sum === target) {
            return [arr[left].index, arr[right].index];
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
};

// ############################### Use following for Practice ###############################

// ----------------------------------------------------------------------
// 1. Brute Force
// Time: O(n²), Space: O(1)
// try every pair — nested loop, no extra space
// ----------------------------------------------------------------------

// var twoSum = function(nums, target) {

// };

// ----------------------------------------------------------------------
// 2. Hash Map
// Time: O(n), Space: O(n)
// one pass with a hashmap — store seen numbers, look up the complement
// ----------------------------------------------------------------------

// var twoSum = function(nums, target) {

// };

// ----------------------------------------------------------------------
// 3. Sort + Two Pointers
// Time: O(n log n), Space: O(n)
// sort + two pointers — preserve original indices before sorting
// ----------------------------------------------------------------------

// var twoSum = function(nums, target) {

// };
