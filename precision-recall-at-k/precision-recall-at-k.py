def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    rec_set = set(recommended[:k])
    rel_set = set(relevant)

    hit  = 0
    for x in rec_set:
        if x in rel_set:
            hit +=1

    return [hit/k, hit/len(rel_set)]
