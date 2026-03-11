algorithm = """
QUICKSORT(A, low, high)

if low < high

    p = PARTITION(A, low, high)

    QUICKSORT(A, low, p-1)
    QUICKSORT(A, p+1, high)

PARTITION:

pivot = A[high]
i = low - 1

for j = low to high-1

    if A[j] <= pivot

        i = i + 1
        swap A[i], A[j]

swap A[i+1], A[high]

return i+1
"""

time_complexity = """
Best Case : O(n log n)
Average Case : O(n log n)
Worst Case : O(n^2)
"""

space_complexity = """
O(log n)
"""