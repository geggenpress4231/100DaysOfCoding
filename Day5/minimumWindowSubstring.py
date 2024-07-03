class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_dict = {}
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1

        required = len(t_dict)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        min_len = float('inf')
        min_str = ""

        # Start expanding the right boundary of our window
        while r < len(s):
            character = s[r]
            if character in t_dict:
                window_counts[character] = window_counts.get(character, 0) + 1
                if window_counts[character] == t_dict[character]:
                    formed += 1
            
            # Try and contract the window till the point it ceases to be 'desirable'
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_str = s[l:r+1]
                
                # The character at the position pointed by `l` is going out of the window
                if character in window_counts:
                    window_counts[character] -= 1
                    if window_counts[character] < t_dict[character]:
                        formed -= 1
                
                l += 1  # Contract the window

            # Keep expanding the window once contracted
            r += 1
        
        return min_str
