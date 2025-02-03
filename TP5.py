import heapq as hq

def create_adjacency_matrix():
    size = 10
    matrix = [[float('inf')] * size for _ in range(size)]
    edges = [
        (0, 1, 4), (0, 2, 1),
        (1, 5, 3),
        (2, 3, 8), (2, 5, 7),
        (3, 7, 5),
        (4, 8, 2), (4, 7, 2),
        (5, 4, 1), (5, 7, 1),
        (6, 8, 4), (6, 9, 4),
        (7, 6, 7), (7, 9, 7), (7, 8, 6),
        (8, 9, 1)
    ]
    for u, v, w in edges:
        matrix[u][v] = matrix[v][u] = w
    return matrix

def display_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
        print(" ".join(f"{x if x != float('inf') else '∞':>3}" for x in row))

def find_shortest_path(matrix, src, dest):
    size = len(matrix)
    dist = [float('inf')] * size
    dist[src] = 0
    prev = [-1] * size
    pq = [(0, src)]
    
    while pq:
        curr_dist, curr_node = hq.heappop(pq)
        if curr_dist > dist[curr_node]:
            continue
        for neighbor, weight in enumerate(matrix[curr_node]):
            if weight != float('inf'):
                new_dist = curr_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = curr_node
                    hq.heappush(pq, (new_dist, neighbor))
    
    path = []
    node = dest
    while node != -1:
        path.append(node)
        node = prev[node]
    path.reverse()
    
    return path, dist[dest]

if __name__ == "__main__":
    matrix = create_adjacency_matrix()
    display_matrix(matrix)
    
    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "L", "M"]
    source = input("\nEnter source node (A-M): ").upper()
    target = input("Enter target node (A-M): ").upper()
    
    src_index, dest_index = labels.index(source), labels.index(target)
    path, distance = find_shortest_path(matrix, src_index, dest_index)
    
    print("\nShortest Path:", " -> ".join(labels[node] for node in path))
    print("Weighted Sum of Shortest Path:", distance)
