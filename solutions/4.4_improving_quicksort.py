from random import randint


def partition3(array, left, right):
    """
    Partition array into 3 parts: 
    p1. array[left:m1-1]: element < pivot
    p2. array[m1:m2]: element = pivot (the left most element in initial array)
    p3. array[m2+1:right]: element > pivot
    To compared with 2 part partition, this 3 part partition helps to handle equal elements.
    """
    pivot = array[left]
    m1, m2 = left , left
    for i, element in enumerate(array[left + 1:right+1]):
        ind = left + i + 1
        if element < pivot:
            if ind == m2 + 1:
                array[m1], array[ind] = element, pivot
            else:
                array[m1], array[m2+1], array[ind] = element, pivot, array[m2+1]
            m1 += 1
        elif element == pivot: 
            array[m2+1], array[ind] = pivot, array[m2+1]
        m2 += 1        
    return m1, m2


def randomized_quick_sort(array, left, right):
    """
    Algo: 
    Randomly choose a number between left and right to be the pivot
    Sort elements smaller to the pivot to its left and those greater to the pivot to its right.
    Recursively repeat the process until the initial array is compmetely sorted.
    """
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    # input_n = 10
    # elements = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # input_n = 7
    # elements = [2, 3, 9, 2, 2, 1, 1]

    # input_n = 5
    # elements = [2, 3, 9, 2, 9]

    # input_n = 5
    # elements = [9, 3, 9, 2, 2]

    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
