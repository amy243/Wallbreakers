'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
link:https://leetcode.com/problems/two-sum
'''
class Solution(object):
    def twoSum(self, nums, target):
        x=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    x.append (i)
                    x.append(j)

                    return (x)
