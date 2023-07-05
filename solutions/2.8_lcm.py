def naive_lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False

def gcd(a,b):
    if b==0:
        d = a
    else:
        d = gcd(b, a % b)
    return d


def lcm(a, b):
    # note that lcm(a,b) = a*b/gcd(a,b)
    return int(a*b/gcd(a,b))


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

