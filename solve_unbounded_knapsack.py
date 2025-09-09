import math


def solve_unbounded_knapsack(
    weights: list[int], values: list[int], capacity: int
) -> int:
    n = len(values)

    dp = [0 for _ in range(capacity + 1)]

    for c in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= c:

                dp[c] = max(dp[c], values[i] + dp[c - weights[i]])

    return dp[capacity]
