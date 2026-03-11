algorithm = """
TRAVELLING SALESMAN PROBLEM (TSP)

Input:
    Graph with n cities

Output:
    Minimum cost tour visiting each city once

Procedure:

1. Start from the first city.
2. Generate all permutations of remaining cities.
3. For each permutation:
       compute tour cost.
4. Keep track of minimum cost path.
5. Return optimal path.
"""

time_complexity = """
O(n!)
"""

space_complexity = """
O(n)
"""