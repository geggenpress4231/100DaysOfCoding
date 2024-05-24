class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        
        # Helper function to create a frequency count dictionary
        def char_count(s):
            count = {}
            for char in s:
                count[char] = count.get(char, 0) + 1
            return count
        
        p_count = char_count(p)
        s_count = char_count(s[:len(p) - 1])  # Initialize with first len(p) - 1 characters
        
        result = []
        left = 0
        
        for right in range(len(p) - 1, len(s)):
            # Add the current character to the window
            s_count[s[right]] = s_count.get(s[right], 0) + 1
            
            # Check if the current window matches the frequency count of p
            if s_count == p_count:
                result.append(left)
            
            # Remove the left character from the current window
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1
        
        return result

