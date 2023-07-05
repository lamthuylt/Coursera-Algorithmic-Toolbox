from sys import stdin

def best_stop(position, current_stop, tank, stops):
    # find the farest stop (index) from position such that stop<=position+tank
    n = len(stops)
    best_stop = -1
    while current_stop < n and stops[current_stop] <= position+tank:
        best_stop = current_stop
        current_stop += 1
    return best_stop
    
def min_refills(distance, tank, stops):
    # greedy choice: from a beginning position, if there is not any stop within 
    # the tank distance, return impossible. Otherwise, go to the furthest 
    # stop within the tank distance. Then repeat the strategy from the new 
    # position.
    n = len(stops)
    position = 0  
    current_stop = 0
    refill = 0
    
    while position+tank < distance:
        current_stop = best_stop(position, current_stop, tank, stops)
        if current_stop == -1:
            return -1
        else:
            refill += 1
            position = stops[current_stop]
            current_stop += 1
    
    return refill


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
