# 그대로 출력하기
import sys
input = sys.stdin.readline

while True:
    S = input().rstrip()
    if S == "":
        break
    print(S)