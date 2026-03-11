algorithm = """
MASTER THEOREM

Recurrence form:

T(n) = aT(n/b) + f(n)

Steps:

1. Compute log_b(a)

2. Compare f(n) with n^(log_b a)

Case 1:
f(n) = O(n^(log_b a - ε))

T(n) = Θ(n^(log_b a))

Case 2:
f(n) = Θ(n^(log_b a))

T(n) = Θ(n^(log_b a log n))

Case 3:
f(n) = Ω(n^(log_b a + ε))

T(n) = Θ(f(n))
"""

time_complexity = """
Depends on recurrence relation
"""

space_complexity = """
Depends on algorithm
"""