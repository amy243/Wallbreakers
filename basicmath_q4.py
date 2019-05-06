'''
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
link:https://leetcode.com/problems/self-dividing-numbers
'''

class Solution(object):
    def selfDividingNumbers(self, left, right):
        y=[]
        for k in range(left,right+1):
            x=[]
            i=k
            
            y.append(k)
            while i>=1:

                x.append((i%10))
                i=int(i/10)
            z=0
            for j in x:
                if j==0 or k%j!=0:
                    z+=1
            if z>0:
                y.pop()
        return y


