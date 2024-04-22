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
