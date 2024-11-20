#Find all the permuations when given a list of integers

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = [[nums.pop()]]
        while len(nums) > 0:
            num = nums.pop(0)
            new_perms = []
            for perm in self.results:
                new_perms.append([num] + perm)
                for i in range(1, len(perm)):
                    new_perms.append(perm[0:i] + [num] + perm[i:])
                new_perms.append(perm + [num])
            self.results = new_perms
        return self.results