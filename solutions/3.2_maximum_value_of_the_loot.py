from sys import stdin
import numpy as np

def best_item(weights, values):
    n = len(weights)
    value_per_weight_max = 0
    best_id = -1

    for i in range(n):
        if weights[i] > 0:
            v = values[i] / weights[i]
            if v > value_per_weight_max:
                value_per_weight_max = v
                best_id = i

    return best_id


def optimal_value(capacity, weights, values):
    value = 0.
    n = len(weights)
    for i in range(n):
        i = best_item(weights, values)
        w = min(weights[i],capacity)      # np.min([]) returns min of an array vs. min(a,b) returns min between a and b
        value += values[i]*w/weights[i]
        capacity -= w
        weights[i] -= w
    return value


if __name__ == "__main__":
    # input order: n W c1 w1 c2 w2 .... cn wn EOF(Ctrl-Z on Windows)
    # example: 3 9 5000 4 200 3 10 5 Ctrl-Z
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
