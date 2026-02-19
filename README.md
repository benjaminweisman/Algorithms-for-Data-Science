# Algorithms for Data Science

Coursework from Algorithms for Data Science at New College of Florida. Covers foundational algorithm design, asymptotic analysis, and data structures — implemented in Python with NumPy, Matplotlib, and NetworkX.

## Assignments

### 1. Peak Finding
Divide-and-conquer peak finding in 1D and 2D arrays. Includes a linear scan O(N), binary search O(log N), brute-force 2D O(N²), and optimized 2D O(N log N) approaches, with comparison counting and runtime benchmarking.

### 2. Asymptotics and Plotting
Asymptotic growth analysis of common complexity classes (log N, √N, N, N log N, N², N³, 2^N). Includes bubble sort as a reference implementation, function intersection computation with SciPy, and Matplotlib visualizations comparing theoretical vs. actual runtimes.

### 3. Heapsort
Max-heap construction and heap sort implementation with O(N log N) time complexity. Benchmarks sorting performance against theoretical N log N growth.

### 4. Priority Queues
Max-heap-based priority queue applied to a course enrollment system. Students are scored by level (graduate/undergraduate/auditor), major, year, and registration date, then ranked using heap sort to select the top 25 applicants.

### 5. Hashing and Runtime
Hash table with linear probing collision resolution. Uses double hashing (mod 3011, then mod 1021 into a prime-sized table) and measures lookup performance across test keys with histogram visualization.

### 7. Weighted Graphs and Flow Networks
Directed weighted graph analysis using NetworkX: adjacency matrices, Dijkstra's shortest path, path enumeration with probability calculation, graph diameter via eccentricity, and maximum flow (Ford-Fulkerson).

## Tech Stack

- **Language**: Python
- **Libraries**: NumPy, Matplotlib, SciPy, NetworkX

## Topics Covered

- Divide and conquer
- Asymptotic analysis (Big-O, Big-Theta)
- Heaps and heap sort
- Priority queues
- Hash tables and collision resolution
- Graph algorithms (Dijkstra, Ford-Fulkerson)
- Network flow
- Runtime benchmarking and visualization
