import heapq

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(graph, start, goal):
    heap = [(0, start)]
    visited = set()

    while heap:
        cost, current = heapq.heappop(heap)

        if current == goal:
            return cost

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph[current]:
            heapq.heappush(heap, (cost + graph[current][neighbor] + heuristic(neighbor, goal), neighbor))

    return -1

# Example usage
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1}
}

start = (0, 0)
goal = (1, 1)

print("Shortest path cost:", astar(graph, start, goal)) 