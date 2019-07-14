#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # -4 -1 -1 0 1 2 
        res = []
        size = len(nums)
        if size < 3:
            return res
        for i in range(size):
            if nums[i] > 0: 
                break # 如果当前数字大于0，则三数之和一定大于0，所以结束循环
            if i > 0 and nums[i] == nums[i-1]:
                continue # 去重
            L = i + 1
            R = size - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R]
                if sum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1 # 去重
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1 # 去重
                    L += 1
                    R -= 1
                elif sum < 0:
                    L += 1
                elif sum > 0:
                    R -= 1
        return res

