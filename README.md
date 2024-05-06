# Day 1 of 100 Days of Code

## Problem 1: Check for Anagrams

### Description
The task involves determining whether two strings are anagrams of each other. Anagrams are defined as strings that contain the exact same characters with the same frequencies, just arranged differently.

### Approach
The approach to solving the problem involves creating a character frequency profile for each string. This profile maps each character to its frequency in the string. The solution checks if the two profiles are identical, which would confirm that the strings are anagrams.

## Problem 2: Top K Frequent Elements

### Description
This problem requires identifying the top 'k' most frequent elements in a list of integers. The goal is to determine which elements appear most frequently in the list and return them in order of their frequency.

### Approach
The solution involves counting the frequency of each element in the list using a frequency mapping technique. The list of elements is then sorted by their frequency in descending order. Only the top 'k' elements by frequency are returned, providing the list of most frequent elements.

## Problem 3: Group Anagrams

### Description
The challenge is to group words that are anagrams into separate lists. Anagrams are words or phrases that contain the same characters in the same frequencies but arranged differently.

### Approach
To efficiently group anagrams, the approach involves using a dictionary where each key represents a sorted version of the word, ensuring that all anagrams share the same key. Words are processed by sorting their characters, converting these sorted characters into a string, and using this string as a key in the dictionary. Each word is then added to the list corresponding to its key. This ensures that all words grouped under the same key are anagrams of each other, thus effectively grouping them together.

# Day 2 of 100 Days of Code

## Problem 1: Product of Array Except Self

### Description
The task is to create an array `output` such that `output[i]` is equal to the product of all elements in the array except `nums[i]`. This solution must be achieved without using division, and it should run in O(n) time complexity.

### Approach
The solution uses a two-pass algorithm. First, it constructs an array where each element at index `i` contains the product of all the elements to the left of `i`. Then, it adjusts each element by multiplying it with the product of elements to the right of `i`, obtained during a second pass through the array from right to left.

## Problem 2: Two Sum

### Description
This problem requires finding two indices in an array such that their corresponding values add up to a specific target number.

### Approach
The solution involves using a hashmap to store each number's complement (target - number) and its index as you iterate through the array. If a number exists in the hashmap, it means a previous number's complement matches this number, thus forming a pair that adds up to the target.

## Problem 3: Longest Consecutive Sequence

### Description
The goal is to find the length of the longest consecutive elements sequence in an unsorted array. No consecutive numbers should have duplicates.

### Approach
The approach first sorts the array and then iterates through it to find the longest consecutive sequence. The sequence length is incremented when consecutive numbers are found. If a number breaks the sequence, the maximum length is updated if necessary, and the sequence length is reset.

