weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 7
n = len(weights)

dp = []
for i in range(n + 1):
    dp.append([0] * (capacity + 1))

for i in range(1, n + 1):
    w = weights[i - 1]
    v = values[i - 1]
    for c in range(capacity + 1):
        if w <= c:
            if dp[i - 1][c] > dp[i - 1][c - w] + v:
                dp[i][c] = dp[i - 1][c]
            else:
                dp[i][c] = dp[i - 1][c - w] + v
        else:
            dp[i][c] = dp[i - 1][c]

print(dp[n][capacity])
