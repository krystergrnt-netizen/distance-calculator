import math


def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculates the Euclidean distance between two points in a 2D plane."""
    horizontal_difference = x2 - x1
    vertical_difference = y2 - y1

    # Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    return math.sqrt(horizontal_difference**2 + vertical_difference**2)


def main():
    print("=== 2D Distance Calculator ===")

    # Get coordinate inputs from the user
    x1 = float(input("Enter x for Point 1: "))
    y1 = float(input("Enter y for Point 1: "))
    x2 = float(input("Enter x for Point 2: "))
    y2 = float(input("Enter y for Point 2: "))

    # Calculate and display the result formatted to two decimal places
    distance = calculate_distance(x1, y1, x2, y2)
    print(f"\nThe distance between the points is: {distance:.2f}")


if __name__ == "__main__":
    main()
