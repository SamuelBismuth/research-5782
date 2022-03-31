import sys


class WeightedEdge():


    def __init__(self, vertex_a: str, vertex_b: str, weight: int):
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
        self.weight = weight


class CompleteWeightedGraph():
   

    def __init__(self, num_verticies: int, verticies: list, mat_weighted_edges: list):
        self.num_verticies = num_verticies
        self.verticies = verticies
        self.weighted_edges = []
        for vertex_a in range(self.num_verticies):
            current_weighted_edges = []
            for vertex_b in range(self.num_verticies):
                if vertex_a == vertex_b:
                    pass
                current_weighted_edges.append(WeightedEdge(verticies[vertex_a], verticies[vertex_b], mat_weighted_edges[vertex_a][vertex_b]))
            self.weighted_edges.append(current_weighted_edges)

    def get_weight(self, vertex_a, vertex_b):
        return self.weighted_edges[vertex_a][vertex_b].weight
        
    def get_smallest_weight(self, vertex_a, others):
        smaller_weight = sys.maxsize
        smaller_vertex = None
        for vertex in others:
            new_weight = self.get_weight(vertex_a, vertex)
            if smaller_weight > new_weight:
                smaller_weight = new_weight
                smaller_vertex = vertex
        return smaller_vertex


