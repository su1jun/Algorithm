# 친구 네트워크
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

T = int(input())

for _ in range(T):
    parent = dict()
    number = dict()

    F = int(input())

    for _ in range(F):
        a, b = map(str, input().split())

        if a not in parent:
            parent[a] = a
            number[a] = 1

        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a, b)
        print(number[find(a)])