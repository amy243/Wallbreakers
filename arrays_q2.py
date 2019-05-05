class Solution(object):
    def transpose(self, A):
        
        r=len(A)
        c=len(A[0])
        r=len(A)
        M=[[1 for i in range(r)] for j in range(c)]
        for i in range (r):
            for j in range(c):
                M[j][i]=A[i][j]
        return M
                            
