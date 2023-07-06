import sys
input = sys.stdin.readline

# union 번호 찾기
def find_union(x):
    if parent[x] != x:
        parent[x] = find_union(parent[x])
    return parent[x]

# 두 vertex union으로 묶기
def union(a, b):
    a = find_union(a)
    b = find_union(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# vertex, edge 개수
v, e = map(int, input().split())
# parent를 자기 자신으로 초기화
parent = [i for i in range(v)]

# edge 입력 받기
edges = []
for i in range(e):
    a, b = map(int, input().split())
    edges.append((a, b))

# edge 순회하며 union
for a, b in edges:
    union(a, b)
