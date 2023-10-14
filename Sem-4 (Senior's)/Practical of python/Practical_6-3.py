l1=[5,3,1,6,2,4]
def sorting(l1):
    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if(l1[i]>l1[j]):
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
    return l1
ans=sorting(l1)
print(ans)