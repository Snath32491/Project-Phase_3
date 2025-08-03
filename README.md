Social Network Influence Analysis (Phase 3): Optimization, Scaling, and Final Evaluation


Overview

This project implements a scalable and optimized social network analysis tool using Python. It identifies the most influential users (top-K) based on follower relationships, simulating real-world applications like marketing, political campaign analysis, and misinformation tracking.

The code builds upon prior phases by focusing on:
- Optimizing data structures
- Scaling the system to large user bases
- Evaluating performance via rigorous testing

Features

- Models user profiles and their relationships using graph-based data structures
- Computes **influence scores** using degree centrality
- Retrieves **top-K influencers** using a max-heap (priority queue)
- Stress-tested with networks of up to 100,000 users
- Performance benchmarking and graph visualization included


How It Works

1. Data Generation
- Simulates a social graph with `N` users and an average number of followers
- Each user is linked to a randomly selected group of users

2. Influence Scoring
- Influence = Number of followers (degree centrality)
- Influence scores are calculated once and reused via memoization

3. Top-K Influencers
- Uses `heapq.nlargest()` to efficiently retrieve users with the highest influence

4. Benchmarking
- Measures performance (execution time and memory usage) at various scales
- Stores results in `benchmark_results.csv` and plots in `performance_plots.png`


How to Run the Code

Pre-requisites: Python 3.8+, pip
Run the code on python or any environment
Run the benchmark.py code to generate te dataset and the plot_results.py to show graphical repsentation



