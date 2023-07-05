def optimal_summands(n):
    summands = []
    prize = 1
    s = 0
    while s < n:
        if n >= s + prize:
            summands.append(prize)
        else:
            prize = n - (s-prize+1)
            summands[-1] = prize
        s += prize
        prize += 1
    return summands


if __name__ == '__main__':
    # greedy strategy:  
    # if 1 <= n < 1+2           -> k=1 (as n=n)
    # if 1+2 <= n < 1+2+3       -> k=2 (as n=1+(n-1))
    # if 1+2+3 <= n < 1+2+3+4   -> k=3 (as n=1+2+(n-3))
    # ...
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)2

