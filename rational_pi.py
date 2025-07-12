# rational_pi.py
from fractions import Fraction

def rational_pi(n_terms):
    pi_approx = Fraction(0, 1)
    for k in range(n_terms):
        term = Fraction((-1) ** k, 2 * k + 1)
        pi_approx += term
    return 4 * pi_approx

# Example run
if __name__ == "__main__":
    result = rational_pi(1000)
    print(f"Rational Approximation of π: {float(result)}")
    print(f"As Fraction: {result}")
