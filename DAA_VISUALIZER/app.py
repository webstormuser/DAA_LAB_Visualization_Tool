import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import itertools
import time

st.set_page_config(layout="wide")

st.title("DAA Algorithm Visualizer")

menu = st.sidebar.selectbox(
    "Select Algorithm",
    [
        "Insertion Sort",
        "Quick Sort",
        "0/1 Knapsack",
        "Graph Coloring",
        "Travelling Salesman Problem"
    ]
)

# =========================================================
# INSERTION SORT
# =========================================================

if menu == "Insertion Sort":

    st.header("Insertion Sort")

    st.subheader("Algorithm")

    st.code("""
INSERTION-SORT(A, n)

1. for i ← 1 to n-1 do
2.     key ← A[i]
3.     j ← i - 1
4.     while j ≥ 0 and A[j] > key do
5.         A[j+1] ← A[j]
6.         j ← j - 1
7.     A[j+1] ← key
""")

    st.subheader("Time Complexity")

    st.table({
        "Case":["Best","Average","Worst"],
        "Complexity":["O(n)","O(n²)","O(n²)"]
    })

    st.subheader("Space Complexity")

    st.write("O(1) (In-place sorting)")

    arr_input = st.text_input("Enter numbers separated by comma","5,2,9,1,5,6")

    arr = list(map(int,arr_input.split(",")))

    placeholder = st.empty()

    if st.button("Start Sorting"):

        A = arr.copy()

        for i in range(1,len(A)):

            key = A[i]
            j = i-1

            while j>=0 and A[j]>key:

                A[j+1] = A[j]
                j -= 1

                fig,ax = plt.subplots()
                ax.bar(range(len(A)),A)
                ax.set_title("Insertion Sort Step")

                placeholder.pyplot(fig)
                time.sleep(1)

            A[j+1] = key

        st.success("Sorting Completed")


# =========================================================
# QUICK SORT
# =========================================================

elif menu == "Quick Sort":

    st.header("Quick Sort")

    st.subheader("Algorithm")

    st.code("""
QUICKSORT(A, low, high)

1. if low < high
2.     p ← PARTITION(A, low, high)
3.     QUICKSORT(A, low, p-1)
4.     QUICKSORT(A, p+1, high)

PARTITION(A)

1. pivot ← A[high]
2. i ← low - 1
3. for j ← low to high-1
4.     if A[j] ≤ pivot
5.         i ← i + 1
6.         swap A[i], A[j]
7. swap A[i+1], A[high]
8. return i+1
""")

    st.subheader("Time Complexity")

    st.table({
        "Case":["Best","Average","Worst"],
        "Complexity":["O(n log n)","O(n log n)","O(n²)"]
    })

    st.subheader("Space Complexity")

    st.write("O(log n)")

    arr_input = st.text_input("Enter numbers separated by comma","8,3,1,7,0,10,2")

    arr = list(map(int,arr_input.split(",")))

    chart = st.empty()

    def quicksort(A,l,r):

        if l>=r:
            return

        pivot = A[r]
        i=l

        for j in range(l,r):

            if A[j] < pivot:

                A[i],A[j] = A[j],A[i]
                i+=1

                fig,ax = plt.subplots()
                ax.bar(range(len(A)),A)

                chart.pyplot(fig)
                time.sleep(1)

        A[i],A[r] = A[r],A[i]

        quicksort(A,l,i-1)
        quicksort(A,i+1,r)

    if st.button("Start QuickSort"):

        A = arr.copy()
        quicksort(A,0,len(A)-1)

        st.success("Sorting Completed")


# =========================================================
# KNAPSACK
# =========================================================

elif menu == "0/1 Knapsack":

    st.header("0/1 Knapsack Problem")

    st.subheader("Algorithm")

    st.code("""
KNAPSACK(W, wt[], val[], n)

1. Create table K[n+1][W+1]

2. for i ← 0 to n
3.     for w ← 0 to W
4.         if i = 0 or w = 0
5.             K[i][w] ← 0
6.         else if wt[i-1] ≤ w
7.             K[i][w] ← max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
8.         else
9.             K[i][w] ← K[i-1][w]

10. return K[n][W]
""")

    st.subheader("Time Complexity")

    st.write("O(n × W)")

    st.subheader("Space Complexity")

    st.write("O(n × W)")

    weights = list(map(int,st.text_input("Weights","2,3,4,5").split(",")))
    values = list(map(int,st.text_input("Values","3,4,5,6").split(",")))

    W = st.number_input("Capacity",1,20,5)

    n=len(values)

    table=[[0]*(W+1) for _ in range(n+1)]

    placeholder=st.empty()

    if st.button("Run Knapsack"):

        for i in range(1,n+1):

            for w in range(1,W+1):

                if weights[i-1] <= w:

                    table[i][w] = max(
                        values[i-1]+table[i-1][w-weights[i-1]],
                        table[i-1][w]
                    )

                else:

                    table[i][w] = table[i-1][w]

                placeholder.write(np.array(table))

                time.sleep(0.4)

        st.success("DP Table Completed")


# =========================================================
# GRAPH COLORING
# =========================================================

elif menu == "Graph Coloring":

    st.header("Graph Coloring (Backtracking)")

    st.subheader("Algorithm")

    st.code("""
GRAPH-COLORING(G, m)

1. Assign colors to vertices one by one
2. for each vertex v
3.     for color c ← 1 to m
4.         if color c is safe
5.             assign color c
6.             recursively color remaining vertices
7.         if not possible → backtrack
""")

    st.subheader("Time Complexity")

    st.write("O(m^n)")

    st.subheader("Space Complexity")

    st.write("O(n)")

    n = st.slider("Number of vertices",3,6,4)

    G = nx.cycle_graph(n)

    pos = nx.spring_layout(G)

    colors = ["red","green","blue","yellow"]

    placeholder = st.empty()

    if st.button("Start Coloring"):

        for i in range(n):

            fig,ax = plt.subplots()

        node_colors = [
            colors[j % len(colors)] if j <= i else "lightgray"
            for j in range(n)
        ]

        nx.draw(
            G,
            pos,
            node_color=node_colors,
            with_labels=True,
            node_size=1200
        )

        placeholder.pyplot(fig)

        time.sleep(1)

    st.success("Coloring Completed")


# =========================================================
# TSP
# =========================================================

elif menu == "Travelling Salesman Problem":

    st.header("Travelling Salesman Problem")

    st.subheader("Algorithm")

    st.code("""
TSP(G)

1. Start from first city
2. Generate all permutations of remaining cities
3. Calculate cost of each tour
4. Select minimum cost path
""")

    st.subheader("Time Complexity")

    st.write("O(n!)")

    st.subheader("Space Complexity")

    st.write("O(n)")

    n = st.slider("Number of cities",4,7,5)

    cities = np.random.rand(n,2)

    fig,ax = plt.subplots()

    ax.scatter(cities[:,0],cities[:,1])

    for i,(x,y) in enumerate(cities):
        ax.text(x,y,str(i))

    st.pyplot(fig)

    best_distance = float("inf")

    placeholder = st.empty()

    if st.button("Find Optimal Path"):

        for perm in itertools.permutations(range(1,n)):

            path = (0,) + perm + (0,)

            dist = 0

            for i in range(len(path)-1):

                dist += np.linalg.norm(
                    cities[path[i]] - cities[path[i+1]]
                )

            fig,ax = plt.subplots()

            ax.scatter(cities[:,0],cities[:,1])

            for i,(x,y) in enumerate(cities):
                ax.text(x,y,str(i))

            for i in range(len(path)-1):

                ax.plot(
                    [cities[path[i]][0],cities[path[i+1]][0]],
                    [cities[path[i]][1],cities[path[i+1]][1]]
                )

            placeholder.pyplot(fig)

            time.sleep(0.5)

            if dist < best_distance:

                best_distance = dist
                best_path = path

        st.success(f"Optimal Path: {best_path}")
        st.success(f"Minimum Distance: {best_distance:.2f}")