'''
Given two integers x and y, calculate the Hamming distance.
link:https://leetcode.com/problems/hamming-distance/
'''
class Solution(object):
    def hammingDistance(self, x, y):

        z=x^y
        k=0
        while z>0:
            z=z&(z-1)
            k+=1

        return k
