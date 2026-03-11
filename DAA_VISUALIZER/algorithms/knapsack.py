algorithm = """
0/1 KNAPSACK

Input:
    Capacity W
    Weights wt[]
    Values val[]
    Number of items n

Procedure:

1. Create DP table K[n+1][W+1]

2. for i = 0 to n
       for w = 0 to W

           if i == 0 or w == 0
                K[i][w] = 0

           else if wt[i-1] <= w
                K[i][w] = max(
                    val[i-1] + K[i-1][w-wt[i-1]],
                    K[i-1][w]
                )

           else
                K[i][w] = K[i-1][w]

3. return K[n][W]
"""

time_complexity = """
O(n × W)
"""

space_complexity = """
O(n × W)
"""