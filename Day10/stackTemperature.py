# from typing import List

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = [0] * len(temperatures)
        
#         for i in range(len(temperatures)):
#             right = i + 1
#             while right < len(temperatures) and temperatures[right] <= temperatures[i]:
#                 right += 1
#             if right < len(temperatures):
#                 answer[i] = right - i
#             else:
#                 answer[i] = 0
        
#         return answer
#two pointers but time limit exceeded


from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        
        return answer

