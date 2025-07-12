# chudnovsky.py
from decimal import Decimal, getcontext
import math

# Precision set karo (e.g., 100 decimal places)
getcontext().prec = 100

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def calculate_pi_chudnovsky(n_terms):
    C = 426880 * Decimal(math.sqrt(10005))
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, n_terms):
        M = M * (K**3 - 16*K) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    return pi

if __name__ == "__main__":
    result = calculate_pi_chudnovsky(5)  # 5 terms = very high precision
    print(f"Pi approximation using Chudnovsky algorithm: \n{result}")
