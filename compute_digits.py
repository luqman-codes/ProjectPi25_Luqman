# compute_digits.py
from decimal import Decimal, getcontext

def compute_pi_bbp(n_terms):
    getcontext().prec = n_terms + 5  # extra digits for safety
    pi = Decimal(0)

    for k in range(n_terms):
        pi += (Decimal(1) / (16**k)) * (
            Decimal(4) / (8 * k + 1) -
            Decimal(2) / (8 * k + 4) -
            Decimal(1) / (8 * k + 5) -
            Decimal(1) / (8 * k + 6)
        )

    return +pi  # unary plus applies precision

# Example usage
if __name__ == "__main__":
    digits = compute_pi_bbp(20)
    print(f"BBP π approximation (20 terms):\n{digits}")
