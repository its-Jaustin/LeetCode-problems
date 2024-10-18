# 40. Combination Sum II.py
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#############################

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        self.result = {} #need to use a dict so there are no duplicates
        self.target = target
        self.path = []
        self.helper(0, [], self.c_hash(candidates))
        return [list(x) for x in self.result.keys()]
    def helper(self, s:int, path:list, nums:dict):
        #s: sum, 
        #path: the path, 
        #nums: dict --> (key, count)
        if s == self.target:
            self.result[tuple(path)] = 1 #lists cannot be dict keys
        else:
            #
            for key in nums.keys():
                if nums[key] > 0 and s + key <= self.target:
                    nums[key] -= 1
                    self.helper(s+key, path + [key], nums.copy()) #key is chosen
                nums[key] = 0 #set key to 0 if not chosen

    def c_hash(self, nums:list)->dict: #counts how many times each key is used
        hashed = {}
        for x in nums:
            if x in hashed.keys():
                hashed[x] += 1
            else:
                hashed[x] = 1
        return hashed


        
