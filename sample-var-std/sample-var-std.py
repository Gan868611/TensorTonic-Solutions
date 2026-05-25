import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x_arr = np.array(x)
    sum_dev = 0
    for i in x:
        sum_dev += (i - np.mean(x_arr))**2

    return (sum_dev/(len(x) - 1)),(sum_dev/(len(x) - 1))**0.5 
    