# 세로읽기
import sys
input = sys.stdin.readline

vertical = [""] * 15

for _ in range(5):
    S = input().rstrip()
    for i in range(len(S)):
        vertical[i] += S[i]

print("".join(vertical))
