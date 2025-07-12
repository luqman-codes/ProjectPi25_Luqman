# monte_carlo.py
import random

def calculate_pi(n_points):
    inside_circle = 0

    for _ in range(n_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return 4 * inside_circle / n_points

# Example run
if __name__ == "__main__":
    result = calculate_pi(100000)
    print(f"Monte Carlo π Approximation: {result}")
