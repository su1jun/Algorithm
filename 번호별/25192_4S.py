import sys
input = sys.stdin.readline

N = int(input())
log = set()
ans = 0
for _ in range(N):
    s = input().rstrip()
    if s != "ENTER":
        log.add(s)
    else:
        ans += len(log)
        log = set()
ans += len(log)
print(ans)