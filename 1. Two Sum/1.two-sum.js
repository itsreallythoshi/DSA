// 01 Two Sum (https://leetcode.com/problems/two-sum/)

// Two Sum patterns:
// 1. Brute force: try every pair
// 2. Hash map: for each number, check if its complement was seen before
// 3. Sort + two pointers: works on sorted values, but must preserve original indices

// Two Sum

// 1. Hash Map approach
// Time: O(n)
// Space: O(n)
// Best standard solution for unsorted Two Sum
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Stores: number -> index
    const seen = new Map();

    for (let i = 0; i < nums.length; i++) {
        const current = nums[i];
        const complement = target - current; // the number we need to have seen before

        // If we've already seen the complement,
        // then complement + current = target
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }

        // Store current number after checking,
        // so we don't use the same element twice
        seen.set(current, i);
    }
};

// 2.1 Sort + Two Pointers
// Time: O(n log n) because of sorting
// Space: O(n) because we keep value + original index
// Useful pattern, but not the best standard answer for unsorted Two Sum

// Broken version:
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const sum = nums[left] + nums[right];

        if (sum === target) {
            return [left, right];
        } else if (sum < target) {
            left++;   // need a bigger sum
        } else {
            right--;  // need a smaller sum
        }
    }
};

// Why it's broken:
// Two pointers only works correctly on a sorted array.
// Also, even if we sort nums directly, we'd lose the original indices.

// 2.2 Correct sort + two pointers version
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Keep both the value and its original index
    const arr = nums.map((value, index) => ({ value, index }));

    // Sort by value so two pointers works
    arr.sort((a, b) => a.value - b.value);

    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        const sum = arr[left].value + arr[right].value;

        if (sum === target) {
            // Return original indices, not sorted positions
            return [arr[left].index, arr[right].index];
        } else if (sum < target) {
            left++;   // need a bigger sum
        } else {
            right--;  // need a smaller sum
        }
    }
};

// 3. Brute Force
// Time: O(n^2)
// Space: O(1)
// Simplest approach, checks every pair
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        // Start from i + 1 so we don't reuse the same element
        // and don't check the same pair twice
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
};