'''
Given an integer, write a function to determine if it is a power of two.
link: https://leetcode.com/problems/power-of-two
'''

class Solution(object):
    def isPowerOfTwo(self, n):
     
        if(n==1):
            return('true')
        else:
            while (n>1):
                if n%2==1:
                    return('false')
                else:
                    n/=2

            return('true')
