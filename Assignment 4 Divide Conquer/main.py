import random
from DSA_4 import FindClosestPoints, distance, generate_random_points, BruteForceClosestPoints, FindClosestPointsNaive

# Here let me generate 10 random points.
def main():
    num_points = 10 
    x_range = [0, 10] 
    y_range = [0, 10]

    # Generate random points
    points = generate_random_points(num_points, x_range, y_range)

    print("Generated Points:")
    for point in points:
        print("Horizontal:", round(point.x, 2), "Vertical:", round(point.y, 2))

    closest_pair_dc = FindClosestPoints(points, points[:])  # Divide and Conquer algorithm
    closest_pair_naive = FindClosestPointsNaive(points)  # Naive algorithm

    # Print teh decimal value of 2 points
    print("\nClosest points (Divide and Conquer):")
    print("Point 1 - Horizontal:", round(closest_pair_dc[0].x, 2), "Vertical:", round(closest_pair_dc[0].y, 2))
    print("Point 2 - Horizontal:", round(closest_pair_dc[1].x, 2), "Vertical:", round(closest_pair_dc[1].y, 2))

    print("\nClosest points (Naive):")
    print("Point 1 - Horizontal:", round(closest_pair_naive[0].x, 2), "Vertical:", round(closest_pair_naive[0].y, 2))
    print("Point 2 - Horizontal:", round(closest_pair_naive[1].x, 2), "Vertical:", round(closest_pair_naive[1].y, 2))

    # Checking if the results from both algorithms are the same
    if closest_pair_dc == closest_pair_naive:
        print("\nResults are correct between algorithms.")
    else:
        print("\nResults are differnt between two algorithms.")

if __name__ == "__main__":
    main()



