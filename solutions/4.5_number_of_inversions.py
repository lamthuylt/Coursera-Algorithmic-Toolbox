from itertools import combinations
import numpy as np

def merge_inversions(left,right):
    """ O(n)
    Merge two sorted arrays left and right and count the number of inversions 
    in the merged sequence left-right. 
    
    The number of inversions in the sequence is the number of indices i<j 
    such that left-right_i > left-right_j
    
    This number of inversions is the sum of the number of remaining elements from 
    the left array when an element from the right array is merged. Note that after
    merging one element (from left/right array), we pop this element from the 
    source array.
    """
    result = []
    inversions = 0

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
            inversions += len(left)

    result += left or right

    return result, inversions


def merge_sort_inversions(a):
    """ O(nlogn)
    Merge sort: recursively split the input array into two subarrays until subarrays
    are of length 1. Then recursively merge them into a sorted array until obtaining
    the sorted initial array.

    Count the number of inversions defined as in the previous function.
    """
    n = len(a)

    if n == 1:
        return a, 0
    
    mid = n // 2
    left, inversions_left = merge_sort_inversions(a[:mid])      # !!! from index 0 to mid-1
    right, inversions_right = merge_sort_inversions(a[mid:])    # !!! from index mid to n-1
    merged, inversions_merged = merge_inversions(left, right)
    
    return merged, inversions_left + inversions_right + inversions_merged
    
    

def inversions_naive(a):
    """ O(n^2)
    Go through all possible pairs (i,j)    
    """
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


if __name__ == '__main__':
    # elements = [2, 3, 9, 2, 9]

    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    # print(inversions_naive(elements))
    _, inversions = merge_sort_inversions(elements)
    print(inversions)
