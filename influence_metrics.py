import heapq

def compute_influence_scores(graph):
    follower_count = {user: 0 for user in graph}
    for user, follows in graph.items():
        for followed in follows:
            if followed in follower_count:
                follower_count[followed] += 1
    return follower_count

def top_k_influencers(influence_scores, k=5):
    return heapq.nlargest(k, influence_scores.items(), key=lambda x: x[1])
