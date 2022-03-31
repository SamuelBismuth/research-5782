from abc import ABC, abstractmethod
from graph import WeightedEdge


class Routes(ABC):


    def __init__(self, numroutes: int):
        self.numroutes = numroutes
    
    @abstractmethod
    def add_route_to_routes(self, route: WeightedEdge, index: int):
        pass

    @abstractmethod
    def result(self):
        return None


class RoutesKeepingSums(Routes):


    def __init__(self, numroutes: int):
        super().__init__(numroutes)
        self.sums = 0

    def add_route_to_routes(self, route: WeightedEdge, index: int):
        self.sums += route.weight

    def result(self):
        return self.sums


class RoutesKeepingContents(RoutesKeepingSums):
   
   
    def __init__(self, numroutes: int):
        super().__init__(numroutes)
        self.routes = [[] for _ in range(numroutes)]

    def add_route_to_routes(self, route: WeightedEdge, index: int):
        super().add_route_to_routes(route, index)
        self.routes[index] = route

    def result(self):
        return self.routes