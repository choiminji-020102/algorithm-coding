import sys
import heapq

node, edge = map(int, sys.stdin.readline().split()) 
start = int(sys.stdin.readline())

graph = [[] for _ in range(node+1)]
# print(graph)

for i in range(edge):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))

# print(graph)


def dijkstra(start, graph, node):
    best_dist = [float('inf')] * (node+1)
    best_dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > best_dist[cur_node]:
            continue

        for goal_node, dist in graph[cur_node]:
            new_dist = cur_dist + dist
            if new_dist < best_dist[goal_node]:
                best_dist[goal_node] = new_dist
                heapq.heappush(pq, (new_dist, goal_node))
    
    return best_dist



best_dist = dijkstra(start, graph, node)

for i, d in enumerate(best_dist):
    if i != 0:
        # d이 문자열 'inf'라면 대문자로 바꾸고, 아니면 그대로 출력
        print(str(d).upper())
    