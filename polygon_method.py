# polygon_method.py
import math

def approximate_pi(n_sides):
    radius = 1  # Circle with radius = 1

    # Length of one side of inscribed polygon
    side_length = 2 * radius * math.sin(math.pi / n_sides)
    perimeter = n_sides * side_length

    # π ≈ perimeter / (2 * radius)
    pi_approx = perimeter / (2 * radius)
    return pi_approx

# Example usage
if __name__ == "__main__":
    sides = 96  # Try with 6, 12, 24... 96
    result = approximate_pi(sides)
    print(f"Approximation of π using {sides}-gon: {result}")
