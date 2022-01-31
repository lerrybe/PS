def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형을 표현 (2차원 리스트)
graph = [
  [], # 1번 노드부터인 경우 많기 때문에 0번은 비워줌
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4], 
  [7],
  [2, 6, 8],
  [1, 7],
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9 # 인덱스 0은 사용하지 않게 하기 위해 하나 더해서 정의해둠 (더 직관적)

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
