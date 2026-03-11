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

         K = [[0]*(W+1) for _ in range(n+1)]

        for i in range(1,n+1):

            for w in range(1,W+1):

                if weights[i-1] <= w:

                    K[i][w] = max(
                        values[i-1] + K[i-1][w-weights[i-1]],
                        K[i-1][w]
                    )

                else:
                    K[i][w] = K[i-1][w]

                fig, ax = plt.subplots(figsize=(6,4))

                table = np.array(K)

                ax.imshow(table, cmap="Blues")

                # ADD NUMBERS INSIDE EACH CELL
                for r in range(n+1):
                    for c in range(W+1):

                        ax.text(
                            c,
                            r,
                            str(table[r][c]),
                            ha="center",
                            va="center",
                            color="black",
                            fontsize=11,
                            fontweight="bold"
                        )

                ax.set_title("DP Table Construction")

                ax.set_xlabel("Capacity")

                ax.set_ylabel("Items")

                placeholder.pyplot(fig)

                time.sleep(speed)

        st.success(f"Maximum Profit = {K[n][W]}")

# =====================================================
# GRAPH COLORING
# =====================================================

    elif menu == "Graph Coloring":

        st.header("Graph Coloring Visualization")

        n=st.slider("Vertices",3,6,4)

        G=nx.cycle_graph(n)

        pos=nx.spring_layout(G)

        fig,ax=plt.subplots()

        nx.draw(G,pos,with_labels=True,node_color="lightblue")

        st.pyplot(fig)

# =====================================================
# TSP
# =====================================================

    elif menu == "Travelling Salesman Problem":

        st.header("Travelling Salesman Problem Visualization")

        n=st.slider("Cities",4,7,5)

        cities=np.random.rand(n,2)

        fig,ax=plt.subplots()

        ax.scatter(cities[:,0],cities[:,1])

        for i,(x,y) in enumerate(cities):
            ax.text(x,y,f"C{i}")

        st.pyplot(fig)

# =====================================================
# JOB SEQUENCING
# =====================================================

    elif menu == "Job Sequencing with Deadline":

        st.header("Job Sequencing")

        jobs=["J1","J2","J3","J4","J5"]
        deadlines=[2,1,2,1,3]
        profits=[100,19,27,25,15]

        st.table({
            "Job":jobs,
            "Deadline":deadlines,
            "Profit":profits
        })

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