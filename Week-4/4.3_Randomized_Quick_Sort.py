import random


def partition(array, left, right):
    m2 = left
    for i in range(left + 1, right+1):
        if array[i] <= array[left]:
            m2 += 1
            array[m2], array[i] = array[i], array[m2]
    array[left], array[m2] = array[m2], array[left]
    m1 = left
    for i in range(left, m2):
        if array[i] < array[m2]:
            array[i], array[m1] = array[m1], array[i]
            m1 += 1
    return m1, m2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return

    k = random.randint(left, right)
    array[left], a[k] = a[k], array[left]

    # print("after pivot exchange:", array)
    m1, m2 = partition(array, left, right)
    randomized_quick_sort(array, left, m1-1)
    randomized_quick_sort(array, m2+1, right)


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    l, r = 0, n-1
    randomized_quick_sort(a, l, r)
    for x in a:
        print(x, end=' ')
