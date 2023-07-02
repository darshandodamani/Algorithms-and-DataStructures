import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generate_random_points(num_points, x_range, y_range):
    points = []
    for _ in range(num_points):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        points.append(Point(x, y))
    return points

def FindClosestPoints(X, Y): 
    if len(X) > 3:
        m = len(X) // 2
        l_x = (X[m].x + X[m+1].x) / 2
        X_l = X[:m]
        X_r = X[m+1:]

        p1, p2 = FindClosestPoints(X_l, Y)
        p3, p4 = FindClosestPoints(X_r, Y)
        p5, p6 = Combine(Y, l_x, (p1, p2), (p3, p4))

        return p5, p6
    else:
        return BruteForceClosestPoints(X)

def BruteForceClosestPoints(points):
    n = len(points)
    min_distance = float('inf')
    p5 = p6 = None

    for i in range(n - 1):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                p5, p6 = points[i], points[j]

    return p5, p6

def Combine(Y, l_x, pair1, pair2):
    p1, p2 = pair1
    p3, p4 = pair2

    if p1 is None:
        return p3, p4
    elif p3 is None:
        return p1, p2

    d1 = distance(p1, p2)
    d2 = distance(p3, p4)

    if d1 < d2:
        p5, p6 = p1, p2
        d = d1
    else:
        p5, p6 = p3, p4
        d = d2

    Y_dash = []
    for point in Y:
        if abs(point.x - l_x) < d:
            Y_dash.append(point)

    merge_sort(Y_dash, 0, len(Y_dash) - 1)

    for i in range(len(Y_dash) - 1):
        j = 1
        while j <= 7 and i + j < len(Y_dash):
            d3 = distance(Y_dash[i], Y_dash[i+j])
            if d3 < d:
                p5, p6 = Y_dash[i], Y_dash[i+j]
                d = d3
            j += 1

    return p5, p6

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Sorts the array of points using the merge sort algorithm
# Calculate the midpoint of the array, and sort the left and right subarrays, and merge them back together
# Reference: Psuedocode from Lecture (Divide and Conquer), page 3
def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, r, q)

# Merges two sorted subarrays into a single sorted subarray.
# Calculate the sizes of the left and right subarrays, and create them, and copy the elements from the original array into the left and right subarrays, 
# and merge the left and right subarrays back into the original array. 
# Reference: Psuedocode from Lecture (Divide and Conquer), page 4
def merge(arr, p, r, q):
    n1 = q - p + 2
    n2 = r - q + 1
    L = [None] * n1
    R = [None] * n2

    for i in range(n1 - 1):
        L[i] = arr[p + i]
    L[n1 - 1] = Point(float('inf'), float('inf'))

    for j in range(n2 - 1):
        R[j] = arr[q + j + 1]
    R[n2 - 1] = Point(float('inf'), float('inf'))

    i = j = 0

    for k in range(p, r + 1):
        if L[i].x <= R[j].x:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
