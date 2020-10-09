# python3
def count_merge(seq, l, r, left, right):
    count1, count2 = 0, 0
    for i in seq[l:r]:
        if i == left:
            count1 += 1
        elif i == right:
            count2 += 1
    if count1 > (r - l) // 2 and left != -1:
        return left
    elif count2 > (r - l) // 2 and right != -1:
        return right
    else:
        return -1


def get_majority_element(seq, l, r):
    if l + 1 == r:
        return seq[l]
    elif l + 2 == r:
        return seq[l]
    m = (l + r) // 2
    left = get_majority_element(seq, l, m)
    right = get_majority_element(seq, m, r)
    count_merge(seq, l, r, left, right)


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(int(get_majority_element(arr, 0, n) != -1))



