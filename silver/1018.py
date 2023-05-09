n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

result = 100000

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0: # 시작점과 같아야 하는 것들
                    if board[a][b] != 'W': # 시작점이 'W'인 경우
                        cnt1 += 1
                    else: # 시작점이 'B'인 경우
                        cnt2 += 1
                else:
                    if board[a][b] != 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1

        result = min(result, min(cnt1, cnt2))

print(result)
