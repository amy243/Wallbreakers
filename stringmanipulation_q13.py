'''
Write a function that takes a string as input and reverse only the vowels of a string.
link:https://leetcode.com/problems/reverse-vowels-of-a-string
'''

class Solution(object):
    def reverseVowels(self, s):
        
        vow=['a','e','i','o','u','A','E','I','O','U']
        k=[]
        st=[]
        for i in range(len(s)):
            st.append(s[i])
            if s[i] in vow:
                k.append(s[i])
        x=k[::-1]
        for i in range(len(st)):

            if st[i]in vow:
                st[i]=x.pop(0)
        return(''.join(st))



