# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         left = 0
#         right = len(s1)

#         while right <= len(s2):
#             if self.strcmp(s2[left:right], s1):
#                 return True
#             else:
#                 left += 1
#                 right += 1

#         return False

#     def strcmp(self, s1: str, s2: str) -> bool:
#         return sorted(s1) == sorted(s2)

#optimise

class Solution:
      def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Frequency count of characters in s1
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        
        # Initialize the window with the first len(s1) characters of s2
        for i in range(len(s1)):
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            if s1_count == s2_count:
                return True
            # Add the next character to the window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove the first character of the previous window
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
        
        # Check the last window
        return s1_count == s2_count

