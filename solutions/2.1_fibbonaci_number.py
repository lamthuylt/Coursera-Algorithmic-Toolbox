#---------------------
# Naive algorithm
#---------------------
# slow
def FibRecurs(n):
    if n<=1:
        return 1
    else:
        return FibRecurs(n-1) + FibRecurs(n-2)

#-----------------------
# Efficient algorithmn
#----------------------
def FibList(n):
    F = [0 for i in range(n+1)]
    F[0] = 0
    F[1] = 1
    for i in range(2,n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]


if __name__ == '__main__':
    n = int(input("n="))
    assert n>=2, "Insert n>=2"
    print("Naive algorithm: F({})={}".format(n,FibRecurs(n)))
    print("Efficient algorithm: F({})={}".format(n,FibList(n)))
