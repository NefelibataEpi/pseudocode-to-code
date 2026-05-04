
def dfs(graph, start):
    visited = set()
    dfs_helper(graph, start, visited)


def dfs_helper(graph, node, visited):
    visited.add(node)
    print(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_helper(graph, neighbor, visited)


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A"],
    "D": ["B"],
    "E": ["B"]
}

dfs(graph, "A")