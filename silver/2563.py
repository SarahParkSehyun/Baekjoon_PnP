n=int(input())

array=[[0 for _ in range(101)]for _ in range(101)]

for _ in range(n):
    x,y=map(int,input().split())
    for row in range(x,x+10):
        for col in range(y,y+10):
            array[row][col]=1

answer=0

for i in range(1,101):
    for j in range(1,101):
        if array[i][j]==1:
            answer+=1

print(answer)
