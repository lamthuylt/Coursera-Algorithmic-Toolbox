import math

def change(money):
    return int(math.floor(money/10.) + math.floor((money%10)/ 5.) + money%5)


if __name__ == '__main__':
    m = int(input())
    print(change(m))
