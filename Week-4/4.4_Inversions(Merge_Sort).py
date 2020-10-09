# python3
def merge(array_B, array_C, count):
    array_D = []
    while array_B and array_C:
        b, c = array_B[0], array_C[0]
        if b > c:
            count += 1
            array_D.append(c)
            array_C.pop(0)
        else:
            array_D.append(b)
            array_B.pop(0)
    if array_B:
        array_D.extend(array_B)
    else:
        array_D.extend(array_C)
    return array_D, count


def merge_sort(array_A,count):
    if len(array_A) == 1:
        return array_A, 0
    mid = len(array_A) // 2
    array_B, countb = merge_sort(array_A[0:mid],count)
    # print(array_B)
    count += countb
    array_C, countc = merge_sort(array_A[mid:],count)
    count += countc
    # print(array_C)
    result, count = merge(array_B, array_C, count)
    # print("count:", count)
    return result, count


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(merge_sort(arr[0:n],0)[1])
