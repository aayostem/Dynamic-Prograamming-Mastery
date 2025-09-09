import math


def solve_knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(values)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(1, capacity + 1):

            if weights[i - 1] <= c:

                dp[i][c] = max(
                    dp[i - 1][c], values[i - 1] + dp[i - 1][c - weights[i - 1]]
                )
            else:

                dp[i][c] = dp[i - 1][c]

    return dp[n][capacity]
