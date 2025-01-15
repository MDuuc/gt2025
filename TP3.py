def print_adjacency_matrix(adjacency_list):
    max_node = max(adjacency_list.keys())
    adj_matrix = [[0] * (max_node + 1) for _ in range(max_node + 1)]

    for node, children in adjacency_list.items():
        for child in children:
            adj_matrix[node][child] = 1

    print("Adjacency Matrix:")
    for row in adj_matrix[1:]:
        print(" ".join(map(str, row[1:])))


def inorder_traversal(node, adjacency_list, visited):
    if node is None or visited[node]:
        return

    visited[node] = True
    children = adjacency_list.get(node, [])

    if children:
        inorder_traversal(children[0], adjacency_list, visited)

    print(node, end=" ")

    for child in children[1:]:
        inorder_traversal(child, adjacency_list, visited)


if __name__ == "__main__":
    adj_list = {
        1: [2, 3],
        2: [5, 6],
        3: [4],
        4: [8],
        5: [7],
        6: [],
        7: [],
        8: []
    }

    print_adjacency_matrix(adj_list)

    try:
        start_node = int(input("\nEnter node: "))
        visited_nodes = [False] * (max(adj_list.keys()) + 1)
        print("InOrder Output:")
        inorder_traversal(start_node, adj_list, visited_nodes)
    except ValueError:
        print("Invalid input! Please enter an integer.")
