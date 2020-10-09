# python3
def euclidean_gcd(a, b):
    c = []
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        small = a
        large = b
    else:
        small = b
        large = a
        # print(small, large)
    for i in range(0, small+1):
        c.append(large % small)
        # print(c[i])
        if c[i] == 0:
            break
        if c[i] > small:
            large = c[i]
        else:
            large = small
            small = c[i]
    return small


if __name__ == '__main__':
    num1, num2 = [int(x) for x in input().split()]
    print(euclidean_gcd(num1, num2))