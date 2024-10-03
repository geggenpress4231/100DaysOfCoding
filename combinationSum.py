class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to start with the smallest number
        
        def dfs(i, current_sum, path):
            # If the current sum equals the target, we found a valid combination
            if current_sum == target:
                res.append(path.copy())
                return
            
            # If the sum exceeds the target, stop the exploration
            if current_sum > target:
                return
            
            # Explore further candidates
            for j in range(i, len(candidates)):
                candidate = candidates[j]
                
                # Since the candidates are sorted, break if the candidate exceeds the remaining target
                if candidate > target - current_sum:
                    break
                
                # Include the candidate and recursively explore
                path.append(candidate)
                dfs(j, current_sum + candidate, path)
                path.pop()  # Backtrack
        
        # Start with the first candidate, initial sum 0, and an empty path
        dfs(0, 0, [])
        return res
