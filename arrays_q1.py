class Solution(object):
    def flipAndInvertImage(self, A):
        for i in A:
            for j in range(int(len(i)/2)):
                a=i[j]
                i[j]=i[len(i)-(j+1)]
                i[len(i)-(j+1)]=a
        
        
            for k in range(len(i)):
                if i[k]==1:
                    i[k]=0
                elif i[k]==0:
                    i[k]=1
        return A
