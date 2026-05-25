def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Edge case: If there are no users, return 0.0
    if not recommendations:
        return 0.0
        
    hits = 0
    total_users = len(recommendations)
    
    # zip() lets us loop through both lists simultaneously
    for rec, truth in zip(recommendations, ground_truth):
        # 1. Slice the user's recommendation list to the first K elements
        top_k_set = set(rec[:k])
        truth_set = set(truth)
        
        # 2. Check if their intersection is non-empty
        if top_k_set.intersection(truth_set):
            hits += 1
            
    # 3. Divide hits by the total number of users
    return float(hits / total_users)