import random

def generate_social_network(num_users, avg_followers):
    graph = {}
    for user_id in range(num_users):
        graph[user_id] = set()
        followers = random.sample(range(num_users), min(avg_followers, num_users))
        graph[user_id].update(followers)
    return graph
