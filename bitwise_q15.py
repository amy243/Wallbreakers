'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
link:https://leetcode.com/problems/number-complement
'''
class Solution(object):
    def findComplement(self, num):
        n=bin(num)
        n=str(n)
        p=''
        for i in n[2:]:
            if i=='1':
                i='0'
            else:
                i='1'
            p+=i
        return(int(p,2))
