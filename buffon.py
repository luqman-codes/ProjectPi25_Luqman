# buffon.py
import random
import math

def buffon_needle(num_throws, needle_length=1.0, line_distance=1.0):


    hits = 0

    for _ in range(num_throws):
        y_center = random.uniform(0, line_distance / 2)
        angle = random.uniform(0, math.pi / 2)

        y_tip = (needle_length / 2) * math.sin(angle)

        if y_tip >= y_center:
            hits += 1

    if hits == 0:
        return None  # Avoid division by zero

    return (2 * needle_length * num_throws) / (line_distance * hits)

# Example run
if __name__ == "__main__":
    result = buffon_needle(100000)
    print(f"Buffon's Needle π Approximation: {result}")
