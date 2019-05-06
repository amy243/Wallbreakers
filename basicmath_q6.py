'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
link:https://leetcode.com/problems/plus-one
'''

class Solution(object):
    def plusOne(self, digits):

        z=[]
        y=0
        for i in range(len(digits)):
            y=y*10+digits[i]
        y=y+1
        k=str(y)
        for p in range(len(k)):
            z.append(k[p])

        return z
