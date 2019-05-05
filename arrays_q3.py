class Solution(object):
    def sortArrayByParity(self, A):
        x=[]
        for i in range(0,len(A)):
            if A[i]%2==1:
                x.append(A[i])
        for i in x:
            A.remove(i)
            A.append(i)
        return(A)
