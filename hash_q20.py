'''
Given two strings s and t , write a function to determine if t is an anagram of s.
link: https://leetcode.com/problems/valid-anagram
'''
class Solution(object):
    def isAnagram(self, s, t):

        z={}
        z1={}
        for i in s:
            z[i]=z.get(i,0)+1
        for i in t:
            z1[i]=z1.get(i,0)+1

        return (z==z1)
