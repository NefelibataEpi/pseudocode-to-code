def has_negative_cycle(vertices, edges, source):
    distance = {}

    for vertex in vertices:
        distance[vertex] = float("inf")

    distance[source] = 0

    for _ in range(len(vertices) - 1):
        for from_vertex, to_vertex, weight  in edges:
            if (distance[from_vertex] != float("inf") and 
                distance[to_vertex] > distance[from_vertex] + weight):
                distance[to_vertex] = distance[from_vertex] + weight

    for from_vertex, to_vertex, weight  in edges:
        if (distance[from_vertex] != float("inf") and 
            distance[to_vertex] > distance[from_vertex] + weight):
            return True
        
    return False


def main():
    vertices = ["A", "B", "C"]
    edges = [
        ("A", "B", 1),
        ("B", "C", -2),
        ("C", "A", -2),
    ]
    source = "A"

    print(has_negative_cycle(vertices, edges, source))


if __name__ == "__main__":
    main()