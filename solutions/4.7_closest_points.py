from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_strip(points_x_sorted, min_d_intra):
    n = len(points_x_sorted)
    x_mid = (points_x_sorted[n//2-1].x + points_x_sorted[n//2].x) / 2   # x-coordinate of the middle line
    i1, i2 = n//2-1, n//2  # index of the closest points to the middle line of each subset 
    min_d_inter = float("inf")                                          
    strip = []

    # compute the points in the strip (whose x-distance to the middle line does not exceed min_d_intra)
    while i1 >= 0 and x_mid - points_x_sorted[i1].x <= min_d_intra:
        strip.append(points_x_sorted[i1])
        i1 -= 1
    while i2 < n and points_x_sorted[i2].x - x_mid <= min_d_intra:
        strip.append(points_x_sorted[i2])
        i2 += 1

    # sort the set of points in the strip by their y-coordinate
    strip.sort(key=lambda p: p.y)
    
    # for each point in the strip, we compute its distance to the 7 subsequent points in the range
    len_strip = len(strip)
    for i in range(len_strip):
        for j in range(i+1,min(i+8,len_strip)):
            min_d_inter = min(min_d_inter, distance_squared(strip[i], strip[j]))
    
    return min_d_inter


def minimum_distance_squared_fast(points):
    n = len(points)
    points = sorted(points, key = lambda p: (p.x, p.y))

    if n == 2:
        return distance_squared(points[0], points[1])
    elif n == 3:
        return min(distance_squared(points[0], points[1]), distance_squared(points[1], points[2]))
    
    # split the given n points into 2 halves S1, S2 of n/2 points
    d1 = minimum_distance_squared_fast(points[:n//2])
    d2 = minimum_distance_squared_fast(points[n//2:])
    # find the minimum distance between points in each subset
    min_d_intra = min(d1, d2)

    # find the minimum distance between points from different subsets
    min_d_inter = minimum_distance_strip(points, min_d_intra)
        
    return min(min_d_intra, min_d_inter)
    

def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


if __name__ == '__main__':
    # samples
    # input_points = [Point(0,0), Point(3,4), Point(-2,-2)] 
    # input_points = [Point(4,4), Point(-2,-2), Point(-3,-4), Point(-1,3), Point(2,3), Point(-4,0), Point(1,1), Point(-1,-1), Point(3,-1), Point(-4,2), Point(-2,4)]

    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    # print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
    print("{0:.9f}".format(sqrt(minimum_distance_squared_fast(input_points))))
