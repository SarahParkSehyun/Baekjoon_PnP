n=int(input())
lst=[]

for _ in range(n):
    a,b=map(int,input().split())
    lst.append([a,b])

lst.sort(key=lambda x:(x[1],x[0]))

ans_lst=[]
ans_lst.append(lst[0])

for i in range(1,len(lst)):
    if lst[i][0]>=ans_lst[-1][1]:
        ans_lst.append(lst[i])
#print(ans_lst)
if n==1:
    print(1)
else:
    print(len(ans_lst))



