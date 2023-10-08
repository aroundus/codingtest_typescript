#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 위상 정렬(Topological Sort)의 개념:
# - 방향성이 있는 그래프에서 노드를 선형 순서로 나열하는 알고리즘입니다.
# - 순서는 그래프의 간선 방향을 거스르지 않아야 합니다.
# - 즉, 만약 간선 A → B가 있다면, A는 B보다 선행되어야 합니다.

# 시간 복잡도:
# - 그래프의 노드 수를 V, 간선 수를 E라 할 때, 위상 정렬의 시간 복잡도는 O(V + E)입니다.

# 도식화된 위상 정렬 과정:
# 진입 차수가 0인 노드를 선택 → 선택한 노드와 연결된 간선을 제거 → 
# 진입 차수 갱신 → 진입 차수가 0이 된 노드를 선택 → ... (반복)

# 예시 그래프 도식화:
# 각 노드 옆 괄호 안에는 해당 노드의 진입 차수를 표기하였습니다.
#
# 0(0) --> 1(1) --> 3(2)
#  |       |       |
#  v       v       v
# 2(1) --> 4(2) --> 5(2)


# 위상정렬 과정
# 초기 설정
# 결과 리스트: []
# 큐: []

# 1. 진입 차수 계산
# 진입 차수: 0(0), 1(1), 2(1), 3(1), 4(1), 5(2)

# 2. 진입 차수가 0인 노드(0)를 큐에 추가
# 결과 리스트: []
# 큐: [0]

# 3. 큐에서 노드를 꺼내 결과 리스트에 추가
# 결과 리스트: [0]
# 큐: []

# 4. 현재 노드 0 처리
# 진입 차수: 0(0), 1(0), 2(1), 3(1), 4(1), 5(2)
# 큐: []

# 5. 진입 차수가 0인 노드(1)를 큐에 추가
# 결과 리스트: [0]
# 큐: [1]

# 6. 큐에서 노드를 꺼내 결과 리스트에 추가
# 결과 리스트: [0, 1]
# 큐: []

# 7. 현재 노드 1 처리
# 진입 차수: 0(0), 1(0), 2(1), 3(0), 4(1), 5(2)
# 큐: []

# 8. 진입 차수가 0인 노드(3)를 큐에 추가
# 결과 리스트: [0, 1]
# 큐: [3]

# 9. 큐에서 노드를 꺼내 결과 리스트에 추가
# 결과 리스트: [0, 1, 3]
# 큐: []

# 10. 현재 노드 3 처리
# 진입 차수: 0(0), 1(0), 2(1), 3(0), 4(1), 5(1)
# 큐: []

# 11. 진입 차수가 0인 노드(4)를 큐에 추가
# 결과 리스트: [0, 1, 3]
# 큐: [4]

# 12. 큐에서 노드를 꺼내 결과 리스트에 추가
# 결과 리스트: [0, 1, 3, 4]
# 큐: []

# 13. 현재 노드 4 처리
# 진입 차수: 0(0), 1(0), 2(0), 3(0), 4(0), 5(1)
# 큐: []

# 14. 진입 차수가 0인 노드(5)를 큐에 추가
# 결과 리스트: [0, 1, 3, 4]
# 큐: [5]

# 15. 큐에서 노드를 꺼내 결과 리스트에 추가
# 결과 리스트: [0, 1, 3, 4, 5]
# 큐: []

# 16. 현재 노드 5 처리
# 진입 차수: 0(0), 1(0), 2(0), 3(0), 4(0), 5(0)
# 큐: []

# 17. 위상 정렬 완료
# 결과 리스트: [0, 1, 3, 4, 5]
# 큐: []

from collections import deque

def topological_sort(graph):
    # 1. 진입 차수 계산
    num_nodes = len(graph)
    in_degree = [0] * num_nodes
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # 결과 리스트 초기화
    result = []
    
    # 2. 진입 차수가 0인 노드를 큐에 추가
    queue = deque()
    for node in range(num_nodes):
        if in_degree[node] == 0:
            queue.append(node)
    
    # 3. 위상 정렬 시작
    while queue:
        # a. 큐에서 노드를 꺼내 결과 리스트에 추가
        current_node = queue.popleft()
        result.append(current_node)
        
        # b. 해당 노드에서 나가는 간선 제거 및 진입 차수 갱신
        for neighbor in graph[current_node]:
            in_degree[neighbor] -= 1
            
            # c. 진입 차수가 0이 된 노드 큐에 추가
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 4. 결과 리스트에 모든 노드가 포함되었는지 확인
    if len(result) != num_nodes:
        return "그래프에 사이클이 존재합니다. 위상 정렬 불가능!"
    
    # 5. 위상 정렬 완료
    return result

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [4],
    3: [5],
    4: [5],
    5: []
}

result = topological_sort(graph)
if isinstance(result, list):
    print("위상 정렬 결과:", result)
else:
    print(result)

