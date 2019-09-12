#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] ??
#
class Solution:
    def subsets(self, nums):
        res = []
        res.append([])
        if len(nums) == 0:
            return res
        for i in nums:        
            res.extend([[i] + r for r in res])
        return res        

