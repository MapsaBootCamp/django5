from typing import Dict


class Graph:
    def __init__(self):
        self.adj_matrix: Dict["str", list] = {}

    def add_node(self, node_name: str) -> None:
        if node_name in self.adj_matrix:
            print(f"{node_name} exists")
        else:
            self.adj_matrix[node_name] = []

    def add_vertice(self, node_a: str, node_b: str) -> None:
        if node_a not in self.adj_matrix or node_b not in self.adj_matrix:
            print("yeki az nodeha da graph nist")
        else:
            if node_b not in self.adj_matrix[node_a]:
                self.adj_matrix[node_a].append(node_b)
            if node_a not in self.adj_matrix[node_b]:
                self.adj_matrix[node_b].append(node_a)

    def is_conected(self) -> bool:
        pass

    def short_path(self, node_a, node_b) -> List:
        pass

    def all_path(self, node_a, node_b):
        pass

    def __str__(self):
        return str(self.adj_matrix)


g = Graph()
g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")
g.add_node("e")
g.add_node("f")

g.add_vertice("a", "b")
g.add_vertice("a", "e")
g.add_vertice("b", "c")
g.add_vertice("d", "f")
g.add_vertice("d", "e")

print(g)
