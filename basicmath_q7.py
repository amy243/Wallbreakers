'''
Given a column title as appear in an Excel sheet, return its corresponding column number.
link:https://leetcode.com/problems/excel-sheet-column-number
'''
class Solution(object):
    def titleToNumber(self, s):
        y=0
        for i in s:

            y=y*26+(((ord(i)-ord('A')))+1)

        return(y)
