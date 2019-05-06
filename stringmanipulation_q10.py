'''
Given a word, you need to judge whether the usage of capitals in it is right or not.
link: https://leetcode.com/problems/detect-capital
'''

class Solution(object):
    def detectCapitalUse(self, word):

        t=1
        if word[0].isupper():
            for i in word[1:]:
                if i.isupper():
                    t+=1
            if t==1 or t==len(word):
                return('true')
            else:
                return('false')
        else:
            for i in word[1:]:
                if i.islower():
                    t+=1
            if t==len(word):
                return('true')
            else:
                return('false')


