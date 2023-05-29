n=int(input())

dp_list=[0,1,2,4,0,0,0,0,0,0,0,0,0]


def dp(num):
    if dp_list[num]!=0:
        return dp_list[num]
    else:
        for i in range(4,num+1):
            dp_list[i]=dp_list[i-1]+dp_list[i-2]+dp_list[i-3]
        return dp_list[num]

for i in range(n):
    num=int(input())
    print(dp(num))
