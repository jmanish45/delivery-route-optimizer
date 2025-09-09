import math
from typing import List, Tuple

Point = Tuple[str, float, float]

def euclidean(a: Tuple[float,float], b: Tuple[float,float]) -> float:
    return math.hypot(a[0]-b[0], a[1]-b[1])

def total_route_distance(route: List[Point], return_to_start: bool = True) -> float:
    if not route:
        return 0.0
    dist = 0.0
    for i in range(len(route)-1):
        dist += euclidean((route[i][1], route[i][2]), (route[i+1][1], route[i+1][2]))
    if return_to_start:
        dist += euclidean((route[-1][1], route[-1][2]), (route[0][1], route[0][2]))
    return dist

def nearest_neighbor(warehouse: Point, deliveries: List[Point]) -> List[Point]:
    unvisited = deliveries.copy()
    route = [warehouse]
    current = warehouse
    while unvisited:
        next_p = min(unvisited, key=lambda p: euclidean((current[1],current[2]), (p[1],p[2])))
        route.append(next_p)
        unvisited.remove(next_p)
        current = next_p
    return route

def two_opt(route: List[Point]) -> List[Point]:
    best = route[:]
    improved = True
    def d(a,b):
        return euclidean((a[1],a[2]), (b[1],b[2]))
    while improved:
        improved = False
        n = len(best)
        for i in range(1, n-2):
            for j in range(i+1, n):
                if j - i == 1:
                    continue
                A, B = best[i-1], best[i]
                C, D = best[j-1], best[j % n]
                before = d(A,B) + d(C,D)
                after = d(A,C) + d(B,D)
                if after + 1e-9 < before:
                    best[i:j] = list(reversed(best[i:j]))
                    improved = True
    return best
