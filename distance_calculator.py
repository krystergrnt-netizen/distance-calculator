import math


def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculates the Euclidean distance between two points in a 2D plane."""
    horizontal_difference = x2 - x1
    vertical_difference = y2 - y1

    # Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    return math.sqrt(horizontal_difference**2 + vertical_difference**2)


def calculate_midpoint(x1: float, y1: float, x2: float, y2: float) -> tuple[float, float]:
    """Calculates the midpoint between two points in a 2D plane."""
    return (x1 + x2) / 2, (y1 + y2) / 2


def get_float_input(prompt: str) -> float:
    """Ensures the user inputs a valid number, looping until they do."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    print("=== Enhanced 2D Distance & Midpoint Calculator ===")
    print()

    # Get validated coordinate inputs from the user
    x1 = get_float_input("Enter x for Point 1: ")
    y1 = get_float_input("Enter y for Point 1: ")
    x2 = get_float_input("Enter x for Point 2: ")
    y2 = get_float_input("Enter y for Point 2: ")

    # Perform calculations
    distance = calculate_distance(x1, y1, x2, y2)
    mid_x, mid_y = calculate_midpoint(x1, y1, x2, y2)

    print()
    # Display results
    print(f"The distance between the points is: {distance:.2f}")
    print(f"The midpoint between the points is: ({mid_x:.2f}, {mid_y:.2f})")


if __name__ == "__main__":
    main()
