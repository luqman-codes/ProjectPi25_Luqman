# leibniz.py
def calculate_pi(n_terms):
    pi_approx = 0
    for k in range(n_terms):
        term = (-1)**k / (2*k + 1)
        pi_approx += term
    return 4 * pi_approx

# Example: calculate pi using 1000 terms
if __name__ == "__main__":
    result = calculate_pi(1000)
    print(f"Approximation of π using 1000 terms: {result}")
