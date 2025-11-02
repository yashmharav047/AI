# ===== Simple Graph Using Alphabets =====
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


# ===== Depth-Limited DFS =====
def depth_limited_dfs(graph, start, goal, limit, path=None):
    if path is None:
        path = [start]

    if start == goal:
        return path
    if limit <= 0:
        return None

    for neighbor in graph.get(start, []):
        result = depth_limited_dfs(graph, neighbor, goal, limit - 1, path + [neighbor])
        if result is not None:
            return result
    return None


# ===== Iterative Deepening DFS =====
def iddfs(graph, start, goal, max_depth=10):
    for depth in range(max_depth):
        print(f"Searching with depth limit = {depth}")
        result = depth_limited_dfs(graph, start, goal, depth)
        if result:
            return result
    return None


# ===== Main =====
if __name__ == "__main__":
    start = 'A'
    goal = 'G'
    path = iddfs(graph, start, goal)

    if path:
        print(f"\n✅ Path found: {' -> '.join(path)}")
    else:
        print("\n❌ No path found.")
