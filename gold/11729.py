n=int(input())

def hanoi(n,a,b,c):
    if n==1: #원반 한 개만 있을 때
        print(a,c)
    else:
        hanoi(n-1,a,c,b) #n-1개의 원반 시작 기둥->보조 기둥
        print (a,c) #어떤 기둥에서 어떤 기둥으로 옮겨야 하는지
        hanoi(n-1,b,a,c) #n-1개의 원반 보조 기둥->목표 기둥

print(2**n-1)
hanoi(n,1,2,3)