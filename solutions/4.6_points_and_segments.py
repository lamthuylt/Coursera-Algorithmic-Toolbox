"""
PROBLEM STATEMENT
Given a set of points and a set of segments on a line, compute, for each point, 
the number of segments it is contained in.
Input: A list of segments and a list of points
Output: The number of segments containing each point.

SAMPLE
Segments: [0,5], [7,10]
Points: 1,6,11
Output: 1,0,0

>>> points_cover_fast([0,7], [5,10], [1,6,11])
[1, 0, 0]
>>> points_cover_fast([-10], [10], [-100, 100, 0])
[0, 0, 1]
>>> points_cover_fast([0, -3, 7], [5, 2, 10], [1, 6])
[2, 0] 
>>> points_cover_fast([0, 2, 4], [5, 2, 10], [1, 6, 2, 2])
[1, 1, 2, 2]

ALGO
Concatenate all coordinates of segments and points into an array. By sorting that array,
we can easisly see whether a point is contained in a segment. 
For example, the sorted array of the sample 1 above is [0 (1) 5] (6) [7 10] (11), which 
shows that the point (1) is contained in one segment, while (6) and (11) are not.

TIME COMPLEXITY
O(mnlogmn) -> O(nlogn) (for sorting)
"""
from sys import stdin
from collections import defaultdict


def points_cover_fast(starts, ends, points):
    id_point = defaultdict(set)  # indice of points in the input is a set (instead of a unique number) because points can contain coincident points
    for i, p in enumerate(points):
        id_point[p].add(i)

    # concatenate all coordinates into one line
    line = starts + points + ends 
    label = [0] * len(starts) + [1] * len(points) + [2] * len(ends) # label of priority order in sorting

    # sort all coordinates such that for same coordinates, sort by their label in the order: 
    # start -> point -> end so that if a point coincides a segment extremes, the point will 
    # be placed between two segment's extremes
    line, label = zip(*sorted(zip(line,label), key=lambda x: (x[0], x[1]))) 

    cover = 0   # counter of the number of segments covering a position on the line
    count_covers = [0] * len(points) # counter by points
    for i, p in enumerate(line):
        if label[i] == 0:
            cover += 1            
        elif label[i] == 2:
            cover -= 1
        elif label[i] == 1:
            for ind in id_point[p]:
                count_covers[ind] = cover
    
    return count_covers


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


if __name__ == '__main__':
    ### sample 1
    # input_starts, input_ends = [0,7], [5, 10]
    # input_points = [1, 6, 11]
    # ### sample 2
    # input_starts, input_ends = [-10], [10]
    # input_points = [-100, 100, 0]
    # ### sample 3
    # input_starts, input_ends = [0, -3, 7], [5, 2, 10]
    # input_points = [1, 6]
    # ### sample 4
    # input_starts, input_ends = [0, 2, 4], [5, 2, 10]
    # input_points = [1, 6, 2, 2]

    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    # output_count = points_cover_naive(input_starts, input_ends, input_points)
    output_count = points_cover_fast(input_starts, input_ends, input_points)
    print(*output_count)
