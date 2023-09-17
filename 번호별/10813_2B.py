# 바구니 뒤집기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
baskets = [i for i in range(1, N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    baskets[a-1:b] = reversed(baskets[a-1:b])

print(*baskets)