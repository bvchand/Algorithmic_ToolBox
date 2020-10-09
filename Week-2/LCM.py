# python3
def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def compute_lcm(x, y):
    lcm = int((x * y)/compute_gcd(x,y))
    return lcm


if __name__ == '__main__':
    n1, n2 = [int(x) for x in input().split()]
    if n1 < n2:
        n1, n2 = n2, n1
    print(compute_lcm(n1, n2))