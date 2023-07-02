import random
import math

#points in the 2D plane and initiate them
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
# generate random points
def generate_random_points(num_points, x_range, y_range):
    points = []
    for _ in range(num_points):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        points.append(Point(x, y))
    return points

#finding the lefymost and lowermost points
def leftmost_lowest(points):
    return min(points, key=lambda p: (p.x, p.y))

#with respect to the leftmost and lowermost point, finding the polar angle
def polar_angle(p0, p1):
    x0, y0 = p0.x, p0.y
    x1, y1 = p1.x, p1.y
    return math.atan2(y1 - y0, x1 - x0)

#in counter clockwise direction, finding the turn
def turns_left(p0, p1, p2):
    x0, y0 = p0.x, p0.y
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) > 0

#mergesort algorithm as per the previous assignment
def merge_sort(arr, p, r, p0):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q, p0)
        merge_sort(arr, q + 1, r, p0)
        merge(arr, p, r, q, p0)

# merge function for merge sort little modification as per the previous assignment
def merge(arr, p, r, q, p0):
    n1 = q - p + 1
    n2 = r - q
    L = [None] * n1
    R = [None] * n2

    for i in range(n1):
        L[i] = arr[p + i]
    for j in range(n2):
        R[j] = arr[q + j + 1]

    i = j = 0
    k = p

    while i < n1 and j < n2:
        if polar_angle(p0, L[i]) <= polar_angle(p0, R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Gramham's Scan Algorithm to find the convex hull
def graham_scan(X):
    p0 = leftmost_lowest(X)
    Q = [p for p in X if p != p0]
    merge_sort(Q, 0, len(Q) - 1, p0)
    S = [p0, Q[0], Q[1]]

    for i in range(2, len(Q)):
        while len(S) >= 2 and not turns_left(S[-2], S[-1], Q[i]):
            S.pop()
        S.append(Q[i])

    return S

