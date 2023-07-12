from random import randint


def partition3(array, left, right):
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
