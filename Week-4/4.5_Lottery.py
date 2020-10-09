# python3
# def naive_compute_lottery(seg, pt, segments, points):
#     x = 0
#     result = []
#     while x < pt:
#         count = 0
#         for i in range(0, seg):
#             if (points[x] >= segments[i][0]) and (points[x] <= segments[i][1]):
#                 count += 1
#         result.append(count)
#         x += 1
#     for j in result:
#         print(j, end=' ')


def fast_compute_lottery(points, lst):
    count = 0
    result = {}
    lst.sort()
    for i in lst:
        if i[1] == 'l':     count += 1
        elif i[1] == 'r':       count -= 1
        else:
            result[i[0]] = count
    for j in points:
        print(result[int(j)], end=' ')


if __name__ == '__main__':
    lst = []
    # segments = []
    s, p = [int(x) for x in input().split()]
    for i in range(s):
        a, b = [int(x) for x in input().split()]
        lst.append([a, 'l'])
        lst.append([b, 'r'])
        # segments.append([a, b])
    points = [int(x) for x in input().split()]
    for i in points:
        lst.append([i, 'p'])
    # naive_compute_lottery(s, p, segments, points)
    fast_compute_lottery(points, lst)
