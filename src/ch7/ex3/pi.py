"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

import math

def factorial(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def estimate_pi():
    """Computes an estimate of pi.

    Algorithm due to Srinivasa Ramanujan, from 
    http://en.wikipedia.org/wiki/Pi
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)
        term = num / den
        total += term

        if abs(term) < 1e-15:
            break
        k += 1
    total = factor * total

    return 1 / total

if __name__ == '__main__':
    estimate_pi = estimate_pi()
    print("estimate pi =",estimate_pi)
    print("math pi =", math.pi)
    print("diff:", abs(estimate_pi - math.pi))
