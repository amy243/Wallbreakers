'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
link:https://leetcode.com/problems/single-number
'''
class Solution(object):
    def singleNumber(self, nums):

        res=0
        for i in nums:
            res^=i
        return res
