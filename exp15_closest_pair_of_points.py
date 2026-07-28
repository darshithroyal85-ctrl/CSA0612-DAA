import math


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force(points, left, right):
    min_dist = float('inf')
    closest_pair = (None, None)
    for i in range(left, right):
        for j in range(i + 1, right):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                closest_pair = (points[i], points[j])
    return min_dist, closest_pair


if __name__ == "__main__":
    points = [(1, 2), (4, 5), (7, 8), (3, 1)]
    points.sort(key=lambda p: p[0])

    min_dist, closest_pair = brute_force(points, 0, len(points))

    print(f"Closest pair: {closest_pair[0]}-{closest_pair[1]}")
    print(f"Distance = {min_dist}")
