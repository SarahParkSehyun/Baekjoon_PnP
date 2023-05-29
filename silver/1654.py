k,n=map(int,input().split())

cable=[]

for _ in range(k):
    length=int(input())
    cable.append(length)

start,end=1,max(cable)
ans=0

while start<=end:
    mid=(start+end)//2
    sum=0
    for c in cable:
        sum+=c//mid
    if sum>=n:
        start=mid+1
        ans=mid
    else:
        end=mid-1

print(ans)