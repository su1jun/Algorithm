import sys
input = sys.stdin.readline

arr = [[0] * 1508 for _ in range(1508)]
ld = [[0] * 808 for _ in range(808)]
rd = [[0] * 808 for _ in range(808)]
lu = [[0] * 808 for _ in range(808)]
ru = [[0] * 808 for _ in range(808)]

N, M = map(int, input().split())

# 광산 값 받기
for i in range(N):
    for j in range(M):
        arr[i][j] = []

for i in range(N):
    for j in range(N):
        arr[i][j] = []

for i in range(N):
    for j in range(N):
        
        arr[i][j] = []