"""
---------------------------------
MAXIMUM PAIRWISE PRODUCT PROBLEM
---------------------------------
Find the maximum product of two distinct numbers in a sequence of non-negative integers.
Input: A sequence of non-negative integers.
Output: The maximum value that can be obtained by multiplying two different elements from the sequence.

Input format. 
The first line contains an integer n. 
The next line contains n non-negative integers a1;:::;an (separated by spaces).
Output format. 
The maximum pairwise product.
Constraints. 2 ≤ n ≤ 2 · 105; 0 ≤ a1;:::;an ≤ 2 · 105.

Sample 1.
Input:
3
1 2 3
Output:
6

Sample 2.
Input:
10
7 5 14 2 8 8 10 1 2 3
Output:
140
"""


def maximum_pairwise_product(n,numbers):
    # find the maximum number's index
    for i in range(n):
        if (i==0) or (numbers[i]>numbers[ind1]):
            ind1 = i
    # find the second maximum number's index
    ind2 = -1
    for i in range(n):
        if (i!=ind1) and ((ind2==-1) or (numbers[i]>numbers[ind2])):
            ind2 = i
    return numbers[ind1]*numbers[ind2]




if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int,input().split()))
    print(maximum_pairwise_product(n,numbers))
