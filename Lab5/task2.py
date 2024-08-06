from collections import deque

def bfs_find_target(graph, start, target):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(f"Visiting {vertex}")
        
        if vertex == target:
            print(f"Found target {target}")
            return True
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    print(f"Target {target} not found")
    return False

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': ['D'],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': [],
}

# Starting BFS from vertex 'A' to find 'L'
print("BFS traversal to find 'L' starting from vertex 'A':")
bfs_find_target(graph, 'A', 'L')
