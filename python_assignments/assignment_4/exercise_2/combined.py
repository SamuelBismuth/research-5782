from typing import Callable, Any
from graph import CompleteWeightedGraph
from routes import Routes
import outputtypes as out


def travelling_salesman(algorithm: Callable, numcities: int, distances: list, cities_name:list = None, outputtype: out.OutputType=out.TravellingContent):
    """
    >>> travelling_salesman(algorithm=alphabetical, numcities=2, distances=[[0, 1],[2, 0]])
    'start = 0 -> 1 (distance: 1), 1 -> 0 (distance: 2). Total distance = 3'
    >>> travelling_salesman(algorithm=alphabetical, numcities=4, distances=[[0, 1, 3, 4],[2, 0, 1, 2],[4, 2, 0, 4],[2, 3, 4, 0]])
    'start = 0 -> 1 (distance: 1), 1 -> 2 (distance: 1), 2 -> 3 (distance: 4), 3 -> 0 (distance: 2). Total distance = 8'
    >>> travelling_salesman(algorithm=alphabetical, numcities=4, distances=[[0, 1, 3, 4],[2, 0, 1, 2],[4, 2, 0, 4],[2, 3, 4, 0]], cities_name=['Tlv', 'Jerusalem', 'Haifa', 'Paris'])
    'start = Tlv -> Jerusalem (distance: 1), Jerusalem -> Haifa (distance: 1), Haifa -> Paris (distance: 4), Paris -> Tlv (distance: 2). Total distance = 8'
    >>> travelling_salesman(algorithm=alphabetical, numcities=4, distances=[[0, 1, 3, 4],[2, 0, 1, 2],[4, 2, 0, 4],[2, 3, 4, 0]], outputtype=out.TravellingSum)
    'Total distance = 8'
    >>> travelling_salesman(algorithm=greedy, numcities=2, distances=[[0, 1],[2, 0]])
    'start = 0 -> 1 (distance: 1), 1 -> 0 (distance: 2). Total distance = 3'
    >>> travelling_salesman(algorithm=greedy, numcities=4, distances=[[0, 1, 3, 4],[2, 0, 1, 2],[4, 2, 0, 4],[2, 3, 4, 0]])
    'start = 0 -> 1 (distance: 1), 1 -> 2 (distance: 1), 2 -> 3 (distance: 4), 3 -> 0 (distance: 2). Total distance = 8'
    >>> travelling_salesman(algorithm=greedy, numcities=4, distances=[[0, 40, 3, 4],[2, 0, 10, 1],[40, 2, 0, 4],[21, 3, 45, 0]])
    'start = 0 -> 2 (distance: 3), 2 -> 1 (distance: 2), 1 -> 3 (distance: 1), 3 -> 0 (distance: 21). Total distance = 27'
    >>> travelling_salesman(algorithm=greedy, numcities=4, distances=[[0, 40, 3, 4],[2, 0, 10, 1],[40, 2, 0, 4],[21, 3, 45, 0]], cities_name=['Tlv', 'Jerusalem', 'Haifa', 'Paris'], outputtype=out.TravellingSum)
    'Total distance = 27'
    >>> travelling_salesman(algorithm=alphabetical, numcities=2, distances=[[0, 1],[2, 0]], cities_name=['Tlv', 'Jerusalem'])
    'start = Tlv -> Jerusalem (distance: 1), Jerusalem -> Tlv (distance: 2). Total distance = 3'
    >>> travelling_salesman(algorithm=greedy, numcities=4, distances=[[0, 40, 3, 4],[2, 0, 10, 1],[40, 2, 0, 4],[21, 3, 45, 0]], cities_name=['Tlv', 'Jerusalem', 'Haifa', 'Paris'], outputtype=out.TravellingSum)
    'Total distance = 27'
    >>> travelling_salesman(algorithm=greedy, numcities=4, distances=[[0, 40, 3, 4],[2, 0, 10, 1],[40, 2, 0, 4],[21, 3, 45, 0]], cities_name=['Tlv', 'Jerusalem', 'Haifa', 'Paris'])
    'start = Tlv -> Haifa (distance: 3), Haifa -> Jerusalem (distance: 2), Jerusalem -> Paris (distance: 1), Paris -> Tlv (distance: 21). Total distance = 27'
    """    
    if cities_name is None:
        cities_name = list(range(numcities))
    cities = dict(zip(list(range(numcities)),cities_name))
    routes =  outputtype.create_empty_routes(numcities)
    graph = CompleteWeightedGraph(numcities, cities, distances)
    algorithm(routes, graph)
    return outputtype.extract_output_from_routes(routes)

def alphabetical(routes: Routes, graph: CompleteWeightedGraph):
    for vertex in range(graph.num_verticies):
        dest = vertex + 1
        if vertex >= graph.num_verticies - 1:
            dest = 0
        routes.add_route_to_routes(graph.weighted_edges[vertex][dest], vertex)
    return routes

def greedy(routes: Routes, graph: CompleteWeightedGraph):
    vertex = 0
    i = 0
    while len(graph.verticies) > 1:
        graph.verticies.pop(vertex)
        dest = graph.get_smallest_weight(vertex, graph.verticies)
        routes.add_route_to_routes(graph.weighted_edges[vertex][dest], i)
        vertex = dest
        i += 1
    routes.add_route_to_routes(graph.weighted_edges[vertex][0], i)
    return routes


if __name__ == "__main__":

    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))