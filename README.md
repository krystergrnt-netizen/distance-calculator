import math

def calculate_distance():
    # Print the application header banner
    print("=== 2D Distance Calculator ===")
    print()

    # Get the coordinates for the first point from the user
    x1 = float(input("Enter x for Point 1: "))
    y1 = float(input("Enter y for Point 1: "))

    # Get the coordinates for the second point from the user
    x2 = float(input("Enter x for Point 2: "))
    y2 = float(input("Enter y for Point 2: "))

    # Apply the Euclidean distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print()
    # Display the final calculated distance formatted to 2 decimal places
    print(f"The distance between the points is: {distance:.2f}")

if __name__ == "__main__":
    calculate_distance()
