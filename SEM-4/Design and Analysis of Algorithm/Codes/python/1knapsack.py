p=[0,1,2,5,6]
wt=[0,2,3,4,5]
m,n=8,4
ls1=[[0]*8]*4
print(type(ls1))
print(len(ls1))
for i in range(n+1):
    for w in range(m+1):
        if i==0 or w==0:
            ls1[i][w]=0
        elif wt[i]<=w:
            ls1[i][w]=max(p[i]+ls1[i-1][w-wt[i]],ls1[i-1][w])
        else:
            ls1[i][w]=ls1[i-1][w]
print(ls1[n][m])
