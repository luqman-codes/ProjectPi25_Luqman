# fixed_precision_pi.py
from decimal import Decimal, getcontext

def fixed_precision_pi(n_terms, precision):
    getcontext().prec = precision
    pi_approx = Decimal(0)

    for k in range(n_terms):
        term = Decimal((-1) ** k) / Decimal(2 * k + 1)
        pi_approx += term

    return Decimal(4) * pi_approx

# Example run
if __name__ == "__main__":
    result = fixed_precision_pi(1000, 20)
    print(f"Fixed-Precision π Approximation: {result}")
