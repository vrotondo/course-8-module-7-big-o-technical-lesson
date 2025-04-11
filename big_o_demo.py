"""
Big O Demonstration Script

This file runs different versions of a list-summing function to compare how their
performance scales with input size.
"""

from lib.sum_algorithms import sum_list, sum_list_nested
import time

# Define input sizes to test
sizes = [5, 50, 500]

for size in sizes:
    numbers = list(range(size))

    print(f"\nTesting input size: {size}")

    # Time the O(n) version
    start = time.perf_counter()
    sum_list(numbers)
    end = time.perf_counter()
    print(f"O(n) sum_list execution time: {end - start:.6f} seconds")

    # Time the O(n^2) version
    start = time.perf_counter()
    sum_list_nested(numbers)
    end = time.perf_counter()
    print(f"O(n^2) sum_list_nested execution time: {end - start:.6f} seconds")
