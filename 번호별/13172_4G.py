input = __import__('sys').stdin.readline

def pow(n, t):
    if t == 1: return n % mod
    elif t % 2: return n * pow(n, t - 1) % mod
    else:
        p = pow(n, t // 2)
        return p * p % mod

M = int(input())
mod = 1000000007
ans = 0

for _ in range(M):
    N, S = map(int, input().split())
    ans += S * pow(N, mod - 2) % mod
print(ans % mod)