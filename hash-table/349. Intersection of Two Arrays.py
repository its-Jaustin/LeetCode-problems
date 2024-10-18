#349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their 
# intersection
# . Each element in the result must be unique and you may return the result in any order.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #uses a dict, so you only have to interate through each list once. 
        #O(n)
        my_dict = {}
        i = []
        for x in nums1:
            my_dict[x] = 1
        for x in nums2:
            if x in my_dict: 
                i.append(x)
                del my_dict[x]
        return i
