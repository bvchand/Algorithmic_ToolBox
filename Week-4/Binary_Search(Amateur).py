def binary_search(a, b):
    n = a[0]
    a.remove(a[0])
    k = b[0]
    b.remove(b[0])
    result = []
    for i in range(k):
        result.append(None)
        j = 0
        while j < n:
            if a[j] == b[i]:
                result[i] = j
                break
            else:
                j += 1
                continue
        if result[i] is None:
            result[i] = -1
    return result


if __name__ == '__main__':
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A_terms = A[0]
    B_terms = B[0]
    print(binary_search(A, B))
