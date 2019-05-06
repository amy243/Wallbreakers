class Solution(object):
    def isPalindrome(self, s):

        k=""
        for i in s :
            if i.isalnum():
                k += ''.join(i.upper())

        #print(k)
        if k!=k[::-1]:
            return (False)
        else:
            return (True)
