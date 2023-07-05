def naive_gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
    if b != 0:
        a, b = b, a%b
        d = gcd(a,b)
    else:
        d = a
    return d

if __name__ == "__main__":
    a, b = map(int, input().split())
    #print(naive_gcd(a,b))
    print(gcd(a, b))
