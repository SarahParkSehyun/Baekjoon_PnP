n=int(input())
answer=0

for i in range(n):
    word=input()
    letter_lst=[]
    flag=True
    for j in range(len(word)):
        if word[j] not in letter_lst:
            letter_lst.append(word[j])
        elif word[j] in letter_lst and word[j]==letter_lst[-1]:
            continue
        else:
            flag=False
            break
    if flag==True:
        answer+=1

print(answer)

