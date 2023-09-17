# 팰린드롬인지 확인하기
import sys
input = sys.stdin.readline

S = input().rstrip()
i, ans = 0, 1
while i < len(S) / 2:
    if S[i] != S[-(i+1)]: ans = 0
    i += 1
print(ans)