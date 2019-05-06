
'''
Write a function that reverses a string.
link:https://leetcode.com/problems/reverse-string
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:

        def revv(start, stop, st):
            if start<stop:

                st[start],st[stop]=st[stop],st[start]
                revv(start+1,stop-1,st)
        revv(0,len(s)-1,s)
