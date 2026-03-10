import os

# Base project folder
base_dir = "DAA_VISUALIZER"

# Folder structure
folders = [
    base_dir,
    os.path.join(base_dir, "algorithms"),
    os.path.join(base_dir, "datasets")
]

# Files to create
files = [
    os.path.join(base_dir, "app.py"),
    os.path.join(base_dir, "algorithms", "insertion_sort.py"),
    os.path.join(base_dir, "algorithms", "quicksort.py"),
    os.path.join(base_dir, "algorithms", "knapsack.py"),
    os.path.join(base_dir, "algorithms", "graph_coloring.py"),
    os.path.join(base_dir, "algorithms", "tsp.py")
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file in files:
    with open(file, "w") as f:
        pass

print("Project structure created successfully!")