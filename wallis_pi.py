import time
import math

def wallis_pi(n_terms=100000):
    product = 1.0
    for n in range(1, n_terms + 1):
        product *= (4 * n * n) / (4 * n * n - 1)
    return 2 * product

if __name__ == "__main__":
    start = time.time()
    pi_est = wallis_pi()
    end = time.time()

    print("Estimated π using Wallis Product:", pi_est)
    print("Actual π:", math.pi)
    print("Error:", abs(math.pi - pi_est))
    print("Time taken (s):", end - start)
