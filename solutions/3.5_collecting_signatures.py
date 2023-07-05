import os
from sys import stdin
from collections import namedtuple
import numpy as np

Segment = namedtuple('Segment', 'start end')


def sort_by_left_end(segments):
    left_ends = []
    for s in segments:
        left_ends.append(s.start)
    order = np.argsort(left_ends)
    sorted_segments = [Segment(segments[i].start, segments[i].end) for i in order]
    return sorted_segments


def reduce_two_segments(s1, s2):
    # return recdution = s1 intersects s2 if two segments intersect
    # return reduction = s1 unions s2 otherwise    
    if s1.end < s2.start:                               # s1 is strictly on the left of s2
        reduction = -1
    elif s1.start > s2.end:                             # s1 is strictly on the right of s2
        reduction = -1
    elif s1.start <= s2.start and s1.end >= s2.start:   # s1 intersects s2 on the left of s2 (s1 can contain s2)
        reduction = Segment(s2.start, min(s1.end, s2.end))
    elif s1.start >= s2.start and s1.start <= s2.end:   # s1 intersects s2 on the right of s2 (s1 can be contained by s2)
        reduction = Segment(s1.start, min(s1.end, s2.end))
    return reduction


def optimal_points(segments):
    segments = sort_by_left_end(segments)
    n = len(segments)
    points = []
    if n == 1:
        points.append(segments[0].start)
    elif n > 1:
        for i in range(n-1):
            reduction = reduce_two_segments(segments[i], segments[i+1])     
            if reduction == -1:                     # if current and following segments do not intersect
                points.append(segments[i].end)
            else:                                   # if current and following segments intersect
                segments[i+1] = reduction
        points.append(segments[n-1].end)

    return points


if __name__ == '__main__':
    """
    GREEDY STRATEGY 
    1. sort all segments by left end
    2. reduce 2 segments at a time in left end order, starting from reduce(s1,s2), to reduce(reduce(s1,s2), s3),...
    such that if 2 segments intersect then reduction = intersection; otherwise, reduction = s1 + s2
    By that way, the segments left after the reduction process are where the points should be placed.
    the number of segments left is the minimum number of points needed.
    """
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    input_file = "3.5_input.txt"
    with open(input_file, "r") as f:
        input = f.read()
    # input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)


"""
# Input to be copied to 3.5_input.txt file
# Input 1
3
1 3
2 5
3 6

# Input 2
4
4 7
1 3
2 5
5 6
"""
    
