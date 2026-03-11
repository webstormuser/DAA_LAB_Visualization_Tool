import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import itertools
import time

st.set_page_config(layout="wide")

# Import algorithms
from algorithms.insertion_sort import algorithm as ins_algo, time_complexity as ins_time, space_complexity as ins_space
from algorithms.quicksort import algorithm as quick_algo, time_complexity as quick_time, space_complexity as quick_space
from algorithms.knapsack import algorithm as knap_algo, time_complexity as knap_time, space_complexity as knap_space
from algorithms.graph_coloring import algorithm as gc_algo, time_complexity as gc_time, space_complexity as gc_space
from algorithms.tsp import algorithm as tsp_algo, time_complexity as tsp_time, space_complexity as tsp_space
from algorithms.job_sequencing import algorithm as job_algo, time_complexity as job_time, space_complexity as job_space
from algorithms.recurrence_solver import algorithm as rec_algo, time_complexity as rec_time, space_complexity as rec_space

st.title("🚀 Interactive Design & Analysis of Algorithms (DAA) Visualizer Lab")
st.markdown("### 🎓 Learn Algorithms Through Interactive Visualization")

menu = st.sidebar.selectbox(
    "Select Algorithm",
    [
        "Insertion Sort",
        "Quick Sort",
        "0/1 Knapsack",
        "Graph Coloring",
        "Travelling Salesman Problem",
        "Job Sequencing with Deadline",
        "Recurrence Relation Solver"
    ]
)

speed = st.sidebar.slider("Animation Speed",0.1,2.0,0.6)

# Layout
algo_col, vis_col = st.columns([1,2])

# =====================================================
# LEFT PANEL : ALGORITHM
# =====================================================

with algo_col:

    st.subheader("Algorithm & Complexity")

    if menu == "Insertion Sort":
        st.code(ins_algo)
        st.write("Time Complexity:",ins_time)
        st.write("Space Complexity:",ins_space)

    elif menu == "Quick Sort":
        st.code(quick_algo)
        st.write("Time Complexity:",quick_time)
        st.write("Space Complexity:",quick_space)

    elif menu == "0/1 Knapsack":
        st.code(knap_algo)
        st.write("Time Complexity:",knap_time)
        st.write("Space Complexity:",knap_space)

    elif menu == "Graph Coloring":
        st.code(gc_algo)
        st.write("Time Complexity:",gc_time)
        st.write("Space Complexity:",gc_space)

    elif menu == "Travelling Salesman Problem":
        st.code(tsp_algo)
        st.write("Time Complexity:",tsp_time)
        st.write("Space Complexity:",tsp_space)

    elif menu == "Job Sequencing with Deadline":
        st.code(job_algo)
        st.write("Time Complexity:",job_time)
        st.write("Space Complexity:",job_space)

    elif menu == "Recurrence Relation Solver":
        st.code(rec_algo)
        st.write("Time Complexity:",rec_time)
        st.write("Space Complexity:",rec_space)

# =====================================================
# RIGHT PANEL : VISUALIZATION
# =====================================================

with vis_col:

# =====================================================
# INSERTION SORT
# =====================================================

    if menu == "Insertion Sort":

        st.header("Insertion Sort Visualization")

        arr_input = st.text_input("Enter numbers","5,2,9,1,6")

        arr = list(map(int,arr_input.split(",")))

        placeholder = st.empty()

        if st.button("Start Sorting"):

            A = arr.copy()

            for i in range(1,len(A)):

                key = A[i]
                j = i-1

                while j>=0 and A[j] > key:

                    A[j+1] = A[j]

                    fig, ax = plt.subplots()

                    ax.bar(range(len(A)),A,color="skyblue")

                    placeholder.pyplot(fig)

                    time.sleep(speed)

                    j -= 1

                A[j+1] = key

            st.success(f"Sorted Array: {A}")

# =====================================================
# QUICK SORT
# =====================================================

    elif menu == "Quick Sort":

        st.header("Quick Sort Visualization")

        arr_input = st.text_input("Enter numbers","8,3,1,7,0,10,2")

        arr = list(map(int,arr_input.split(",")))

        chart = st.empty()

        def draw(A):

            fig, ax = plt.subplots()

            bars=ax.bar(range(len(A)),A,color="orange")

            for i,b in enumerate(bars):
                ax.text(b.get_x()+b.get_width()/2,b.get_height()+0.2,str(A[i]),ha='center')

            chart.pyplot(fig)

        def quicksort(A,l,r):

            if l>=r:
                return

            pivot=r
            i=l

            for j in range(l,r):

                draw(A)
                time.sleep(speed)

                if A[j] < A[pivot]:

                    A[i],A[j]=A[j],A[i]
                    i+=1

            A[i],A[pivot]=A[pivot],A[i]

            quicksort(A,l,i-1)
            quicksort(A,i+1,r)

        if st.button("Start QuickSort"):

            A = arr.copy()

            quicksort(A,0,len(A)-1)

            draw(A)

            st.success(f"Sorted Array: {A}")

# =====================================================
# KNAPSACK
# =====================================================

    elif menu == "0/1 Knapsack":

        st.header("0/1 Knapsack Visualization")

        weights = list(map(int, st.text_input("Weights", "2,3,4,5").split(",")))
        values = list(map(int, st.text_input("Values", "3,4,5,6").split(",")))

        W = st.number_input("Capacity", 1, 20, 5)

        n = len(values)

        placeholder = st.empty()

        if st.button("Start Visualization"):

        # Correct DP table initialization
            K = [[0 for _ in range(W+1)] for _ in range(n+1)]

            for i in range(1, n+1):

                for w in range(1, W+1):

                    if weights[i-1] <= w:

                        include = values[i-1] + K[i-1][w-weights[i-1]]
                        exclude = K[i-1][w]

                        K[i][w] = max(include, exclude)

                    else:

                        K[i][w] = K[i-1][w]

                # Visualization
                    fig, ax = plt.subplots(figsize=(6,4))

                    table = np.array(K)

                    ax.imshow(table, cmap="Blues")

                    for r in range(n+1):
                        for c in range(W+1):

                            color = "black"

                            if r == i and c == w:
                                color = "red"

                            ax.text(
                            c,
                            r,
                            str(table[r][c]),
                            ha="center",
                            va="center",
                            color=color,
                            fontsize=11,
                            fontweight="bold"
                        )

                    ax.set_title("Knapsack DP Table Construction")
                    ax.set_xlabel("Capacity")
                    ax.set_ylabel("Items")

                    placeholder.pyplot(fig)

                    time.sleep(speed)

        st.success(f"Maximum Profit = {K[n][W]}")

# =====================================================
# =====================================================
# GRAPH COLORING (BACKTRACKING)
# =====================================================

    elif menu == "Graph Coloring":

        st.header("Graph Coloring using Backtracking")

        n = st.slider("Number of Vertices", 3, 12, 5)
        m = st.slider("Number of Colors", 2, 6, 3)

        G = nx.cycle_graph(n)
        pos = nx.spring_layout(G)

        color_palette = ["red","green","blue","yellow","orange","purple"]

        colors = [-1]*n

        placeholder = st.empty()

        def is_safe(v, c):

            for neighbor in G.neighbors(v):
                if colors[neighbor] == c:
                    return False

            return True


        def draw_graph():

            fig, ax = plt.subplots(figsize=(6,4))

            node_colors = []

            for c in colors:
                if c == -1:
                    node_colors.append("lightgray")
                else:
                    node_colors.append(color_palette[c])

            nx.draw(
                G,
                pos,
                node_color=node_colors,
                with_labels=True,
                node_size=1200,
                edgecolors="black",
                ax=ax
            )

            placeholder.pyplot(fig)


        def graph_coloring(v):

            if v == n:
                return True

            for c in range(m):

                if is_safe(v, c):

                    colors[v] = c

                    draw_graph()
                    time.sleep(speed)

                    if graph_coloring(v+1):
                        return True

                    # Backtracking
                    colors[v] = -1

                    draw_graph()
                    time.sleep(speed)

            return False


        if st.button("Start Graph Coloring"):

            draw_graph()

            if graph_coloring(0):

                st.success("Valid Coloring Found")

            else:

                st.error("No Solution Exists with given colors")
# =====================================================
# =====================================================
# =====================================================
# TSP (User Defined Distance Matrix)
# =====================================================

    elif menu == "Travelling Salesman Problem":

        st.header("Travelling Salesman Problem Visualization")

        n = st.number_input("Number of Cities", 3, 7, 4)

        st.subheader("Enter Distance Matrix")

        dist_matrix = []

        for i in range(n):

            row = st.text_input(
                f"Distances from City {i}",
                " ".join(["0"]*n),
                key=f"row{i}"
            )

            row_values = row.replace(",", " ").split()

            if len(row_values) != n:
                st.error(f"Row {i} must contain {n} values")
                st.stop()

            dist_matrix.append(list(map(int,row_values)))

        dist_matrix = np.array(dist_matrix)

        placeholder = st.empty()

        best_cost = float("inf")
        best_path = None

        if st.button("Start TSP"):

            for perm in itertools.permutations(range(1,n)):

                path = (0,) + perm + (0,)

                cost = 0

                for i in range(len(path)-1):

                    cost += dist_matrix[path[i]][path[i+1]]

                fig, ax = plt.subplots(figsize=(6,4))

                G = nx.complete_graph(n)

                pos = nx.circular_layout(G)

                nx.draw(G,pos,with_labels=True,node_color="lightblue",node_size=1000)

            # draw current path
                edges = [(path[i],path[i+1]) for i in range(len(path)-1)]

                nx.draw_networkx_edges(
                    G,
                    pos,
                    edgelist=edges,
                    width=3,
                    edge_color="orange",
                    ax=ax
                )

                ax.set_title(f"Path {path} | Cost = {cost}")

                placeholder.pyplot(fig)

                time.sleep(speed)

                if cost < best_cost:

                    best_cost = cost
                    best_path = path

        st.success(f"Optimal Path: {best_path}")
        st.success(f"Minimum Cost: {best_cost}")

# =====================================================
# JOB SEQUENCING
# =====================================================

    # =====================================================
# JOB SEQUENCING WITH DEADLINE
# =====================================================

    elif menu == "Job Sequencing with Deadline":

        st.header("Job Sequencing with Deadline (Greedy Visualization)")

        jobs = ["J1","J2","J3","J4","J5"]
        deadlines = [2,1,2,1,3]
        profits = [100,19,27,25,15]

        st.table({
        "Job": jobs,
        "Deadline": deadlines,
        "Profit": profits
     })

        placeholder = st.empty()

        if st.button("Start Scheduling"):

            data = list(zip(jobs, deadlines, profits))

            # sort jobs by profit
            data.sort(key=lambda x: x[2], reverse=True)

            max_deadline = max(deadlines)

            slots = [None]*max_deadline
            total_profit = 0

            for job, d, p in data:

                for i in range(min(max_deadline,d)-1,-1,-1):

                    if slots[i] is None:

                        slots[i] = job
                        total_profit += p

                        break

            # Visualization
                fig, ax = plt.subplots(figsize=(6,2))

                for idx, s in enumerate(slots):

                    color = "lightgray" if s is None else "green"

                    rect = plt.Rectangle((idx,0),0.8,0.6,color=color)

                    ax.add_patch(rect)

                    text = "-" if s is None else s

                    ax.text(idx+0.4,0.3,text,
                        ha="center",
                        va="center",
                        fontsize=12)

                ax.set_xlim(0,max_deadline)
                ax.set_ylim(0,1)
                ax.axis("off")

                ax.set_title(f"Processing Job {job} (Profit {p})")

                placeholder.pyplot(fig)

                time.sleep(speed)

            st.success(f"Final Scheduled Jobs: {slots}")
            st.success(f"Maximum Profit: {total_profit}")
# =====================================================
# MASTER THEOREM
# =====================================================

    elif menu == "Recurrence Relation Solver":

        st.header("Master Theorem Solver")

        a=st.number_input("a",1,10,2)
        b=st.number_input("b",2,10,2)

        fn=st.selectbox("f(n)",["1","log n","n","n log n","n^2"])

        if st.button("Solve"):

            log_val=np.log(a)/np.log(b)

            st.write("log_b(a) =",round(log_val,3))