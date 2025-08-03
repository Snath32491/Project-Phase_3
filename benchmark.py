import time
import tracemalloc
import pandas as pd
from generate_dataset import generate_social_network
from influence_metrics import compute_influence_scores, top_k_influencers

def benchmark_top_k(num_users_list, avg_followers=50, k=5):
    times = []
    memories = []

    for num_users in num_users_list:
        graph = generate_social_network(num_users, avg_followers)
        tracemalloc.start()
        start_time = time.time()

        influence_scores = compute_influence_scores(graph)
        _ = top_k_influencers(influence_scores, k)

        elapsed_time = time.time() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        times.append(elapsed_time)
        memories.append(peak / 1024 / 1024)  # Convert to MB

    return pd.DataFrame({
        'Users': num_users_list,
        'TopK_Time (s)': times,
        'Peak Memory (MB)': memories
    })

if __name__ == "__main__":
    user_sizes = [1000, 5000, 10000, 50000, 100000]
    results = benchmark_top_k(user_sizes)
    print(results)
    results.to_csv("benchmark_results.csv", index=False)
