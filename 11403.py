n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# k는 i와 j를 매개하는 역할을 합니다.
for k in range(n):
    for i in range(n):
        for j in range(n):
            """
            i와 j가 직접적으로 연결되어 있거나
            i와 j가 k를 통해 간접적으로 연결되어 있다면 
            값을 1로 설정합니다.
            """
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
               graph[i][j] = 1

for row in graph:
    row = list(map(str, row))
    print(" ".join(row))