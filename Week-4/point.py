import math


def compute_distance(points_set):
    shortest_distance = 0
    for i in range(len(points_set)):
        shortest_distance = math.sqrt((points_set[i][0] - points_set[i+1][0]) * (points_set[i][0] - points_set[i+1][0])) - ((points_set[i][1] - points_set[i+1][1]) * (points_set[i][1] - points_set[i+1][1]))
    return shortest_distance


def sorted_partitions(points):
    d1, d2 = [], []

    if len(points) == 1:
        return 0.0

    points.sort(key=lambda x: x[0])
    print("sorted points:", points)
    mid = len(points) // 2

    # points_set1 = sorted_partitions(points[0:mid])
    # print(points_set1)
    # d1.append(compute_distance(points_set1))
    # points_set2 = sorted_partitions(points[mid:])
    # d2.append(compute_distance(points_set2))
    # print(d1, d2)


if __name__ == '__main__':
    n = int(input())
    pts = []
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        pts.append([a, b])
    sorted_partitions(pts)
