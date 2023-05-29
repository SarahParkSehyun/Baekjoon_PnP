n=int(input())
dictionary={}

for _ in range(n):
    name,log=input().split()
    if log=='enter':
        dictionary[name]=1
    else:
        dictionary[name]-=1

name_lst=list(dictionary.keys())
answer=[]

for name in name_lst:
    if dictionary[name]==1:
        answer.append(name)

answer.sort(reverse=True)

for name in answer:
    print(name)