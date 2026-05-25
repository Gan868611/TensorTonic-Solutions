import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)

    vals, counts = np.unique(x, return_counts=True)
# Find the highest frequency
    max_count = np.max(counts)
    
    # vals is already sorted ascending by np.unique, 
    # so the first match is the smallest mode
    mode_val = float(vals[counts == max_count][0])
    return np.mean(x), np.median(x), mode_val