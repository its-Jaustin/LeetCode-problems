#Given an array nums of distinct integers, return all the possible
#permutations. You can return the answer in any order
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = {}
        nums.sort()
        self.helper(nums, [])
        return [list(x) for x in self.result.keys()]
    def helper(self, nums: List[int], path: List[int]):
        if nums == []:
            self.result[tuple(path)] = 1
            return
        for x in range(len(nums)):
            path_c = path.copy()
            nums_c = nums.copy()
            path_c.append(nums_c.pop(x))
            self.helper(nums_c, path_c)
