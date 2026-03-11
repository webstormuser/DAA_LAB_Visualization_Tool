algorithm = """
INSERTION SORT

for i = 1 to n-1

    key = A[i]
    j = i - 1

    while j >= 0 and A[j] > key

        A[j+1] = A[j]
        j = j - 1

    A[j+1] = key
"""

time_complexity = """
Best Case : O(n)
Average Case : O(n^2)
Worst Case : O(n^2)
"""

space_complexity = """
O(1)
"""