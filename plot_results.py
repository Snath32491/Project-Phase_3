import pandas as pd
import matplotlib.pyplot as plt

# Load results
benchmark_results = pd.read_csv("benchmark_results.csv")

# Plotting
plt.figure(figsize=(12, 5))

# Top-K Time
plt.subplot(1, 2, 1)
plt.plot(benchmark_results['Users'], benchmark_results['TopK_Time (s)'], marker='o')
plt.title('Top-K Retrieval Time vs. Number of Users')
plt.xlabel('Number of Users')
plt.ylabel('Time (seconds)')
plt.grid(True)

# Memory Usage
plt.subplot(1, 2, 2)
plt.plot(benchmark_results['Users'], benchmark_results['Peak Memory (MB)'], color='orange', marker='o')
plt.title('Peak Memory Usage vs. Number of Users')
plt.xlabel('Number of Users')
plt.ylabel('Memory (MB)')
plt.grid(True)

plt.tight_layout()
plt.savefig("performance_plots.png")
plt.show()
