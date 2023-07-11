import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np

def binary_search(keys, query, l, r):
    mid = l + int(np.floor(r-l)/2)
    if (l > r) or (l == r and query != keys[l]):
        return -1
    elif query == keys[mid]:
        return mid
    elif query < keys[mid]:
        return binary_search(keys, query, l, mid)
    elif query > keys[mid]:
        return binary_search(keys, query, mid+1, r)  # index offset mid+1

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    f = open("4.1_input.json", "r")
    lines = f.readlines()
    num_keys = int(lines[0])
    input_keys = list(map(int, lines[1].split()))
    num_queries = int(lines[2])
    input_queries = list(map(int, lines[3].split()))


    # num_keys = int(input())
    # input_keys = list(map(int, input().split()))
    # assert len(input_keys) == num_keys

    # num_queries = int(input())
    # input_queries = list(map(int, input().split()))
    # assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q, 0, num_keys-1), end=' ')
