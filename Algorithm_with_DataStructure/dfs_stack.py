#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 알고리즘의 개념:
#    DFS(깊이 우선 탐색)은 그래프나 트리를 탐색하는 알고리즘 중 하나로,
#    루트 노드(혹은 다른 임의의 노드)에서 시작하여 마지막 노드까지 깊이를 우선하여 탐색하는 알고리즘입니다.
#    스택을 사용하여 구현할 수 있으며, 아래 코드는 스택을 사용한 방법으로 DFS를 구현한 예입니다.

# 2. 예시 입력 / 출력:
#    입력: graph = {1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, start_node = 1
#    출력: [1, 2, 4, 5, 3]

# 3. 알고리즘의 시간 복잡도:
#    O(V + E) (V: 정점의 개수, E: 간선의 개수)

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - 경로 찾기
#    - 사이클 탐지
#    - 그래프 연결 성분 찾기

# 5. DFS 상세 과정(스택 활용):
#    - 시작 노드(1)를 스택에 넣고, 방문 처리를 한다.
#    - 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
#      방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
#    - 위 과정을 스택이 비어있을 때까지 반복한다.

def dfs(graph, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))  # reversed를 사용하여 깊이 우선 탐색을 유지
    return visited

# 그래프를 인접 리스트로 표현
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

# DFS 알고리즘 실행
result = dfs(graph, 1)
print(result)
# 출력: [1, 2, 4, 5, 3]