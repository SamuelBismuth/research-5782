from abc import ABC
from typing import Any, List
from routes import Routes, RoutesKeepingSums, RoutesKeepingContents


class OutputType(ABC):

    
    @classmethod
    def create_empty_routes(cls, numroutes: int) -> Routes:
        pass

    @classmethod
    def extract_output_from_routes(cls, routes: Routes) -> Any:
        pass


class TravellingSum(OutputType):


    @classmethod
    def create_empty_routes(cls, numroutes: int) -> List:
        return RoutesKeepingSums(numroutes)

    @classmethod
    def extract_output_from_routes(cls, routes: List[Routes]) -> List:
        return 'Total distance = {0}'.format(routes.sums)


class TravellingContent(OutputType):


    @classmethod
    def create_empty_routes(cls, numroutes: int) -> List:
        return RoutesKeepingContents(numroutes)

    @classmethod
    def extract_output_from_routes(cls, routes: Routes) -> str:
        answer = 'start = '
        for route in routes.routes:
            answer = answer + '{0} -> {1} (distance: {2}), '.format(route.vertex_a, route.vertex_b, route.weight)
        answer = answer[:-2] + '. Total distance = {0}'.format(routes.sums)
        return answer