from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, source, destination):
        self.edges[source].append(destination)

    def is_path(self, start, target):
        visited_nodes = set()
        nodes_to_visit = deque([start])

        while nodes_to_visit:
            current_node = nodes_to_visit.popleft()

            if current_node == target:
                return True

            visited_nodes.add(current_node)
            
            for neighbor in self.edges[current_node]:
                if neighbor not in visited_nodes and neighbor not in nodes_to_visit:
                    nodes_to_visit.append(neighbor)

        return False

graph = Graph()

edge_list = [
    (1, 2), (2, 5), (3, 6), (4, 6), (6, 7), (4, 7)
]

for src, dest in edge_list:
    graph.add_edge(src, dest)

start = int(input("Start node: "))
target = int(input("End node: "))

if graph.is_path(start, target):
    print("Existed")
else:
    print("Do not exist")
