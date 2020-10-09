# python3
import math


def binary_search(a, low, high, key):
    if high < low:
        return -1

    mid = low + math.floor((high - low) / 2)
    # print("mid, a[mid]:", mid, a[mid])
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a, low, mid-1, key)
    else:
        return binary_search(a, mid+1, high, key)


def compute_result(a, b):
    # prepare the arrays
    n = a[0]
    a.remove(a[0])
    k = b[0]
    b.remove(b[0])

    # traverse through array 'b'
    result = []
    i = 0
    while i < k:
        key = b[i]
        # print("key:", key)
        low = 0
        high = n-1
        # print("result value:", binary_search(a, low, high, key))
        result.append(binary_search(a, low, high, key))
        i += 1

    for x in result:
        print(x, end=' ')


if __name__ == '__main__':
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A_terms = A[0]
    B_terms = B[0]
    compute_result(A, B)

