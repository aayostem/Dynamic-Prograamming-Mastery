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


def can_partition(nums: list[int]) -> bool:
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    n = len(nums)

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target]


def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def length_of_lis(nums: list[int]) -> int:
    if not nums:
        return 0

    n = len(nums)

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]
