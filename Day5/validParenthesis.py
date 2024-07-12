class Solution:
    def isValid(self, s: str) -> bool:
       
        stack = []
    
        matching_bracket = {')': '(', '}': '{', ']': '['}
        
        
        for char in s:
            if char in matching_bracket:
             if not stack or stack[-1] != matching_bracket[char]:
                    return False
             stack.pop()
            else:
               stack.append(char)
        
        return not stack


