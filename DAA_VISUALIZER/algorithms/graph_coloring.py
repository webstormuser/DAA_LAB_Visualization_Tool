algorithm = """
GRAPH-COLORING(G, m)

Input:
    Graph G with n vertices
    m colors

Output:
    Assign colors so that no two
    adjacent vertices share same color

Procedure:

1. Start with first vertex.
2. Try assigning colors 1..m.
3. Check if color is safe.
4. If safe → assign color.
5. Move to next vertex.
6. If no color works → backtrack.
7. Continue until all vertices colored.
"""

time_complexity = """
Worst Case : O(m^n)
"""

space_complexity = """
O(n)
"""