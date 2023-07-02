# Main function
import ASS5_DSA as dsa5
from matplotlib import pyplot as plt

def main():
    num_points = 10
    x_range = (-10, 10)
    y_range = (-10, 10)

    points = dsa5.generate_random_points(num_points, x_range, y_range)  
    convex_hull = dsa5.graham_scan(points)  
    
    # Print the convex hull points
    print("Convex Hull Points:")
    for point in convex_hull:
        print(f"({point.x:.2f}, {point.y:.2f})")

    # Plotting
    hull_x = [point.x for point in convex_hull]
    hull_y = [point.y for point in convex_hull]

    x = [point.x for point in points]  
    y = [point.y for point in points]  
    
    plt.scatter(x, y, color='blue', label='Points')  
    plt.plot(hull_x + [hull_x[0]], hull_y + [hull_y[0]], color='red', label='Convex Hull')  
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Convex Hull using Graham's Scan - \n Assignment 5: Darshan 124753, Prajwal 124729")
    # plt.legend()
    # plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()