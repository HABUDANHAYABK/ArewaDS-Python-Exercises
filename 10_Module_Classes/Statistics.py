# Mean
def calculate_mean(lst):
    """calculate mean of a list of numbers"""
    sum_of_nums = sum(lst)
    mean = sum_of_nums / len(lst)
    return mean

def calculate_median(lst):
    """Calculate median of a list of numbers"""
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2])/2
    else:
        return sorted_lst[n//2]
    
# Mode
def calculate_mode(lst):
    """calculate mode of a list of numbers"""
    frequency_dict = {}
    for num in lst:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1
    max_frequency = max(frequency_dict.values())
    modes = [num for num, freq in frequency_dict.items() if freq == max_frequency]
    return modes

# Range
def calculate_range(lst):
    """Caluclate the range of a list of numbers"""
    return max(lst) - min(lst)

# Variance
def calculate_variance(lst):
    """Caluclate the variance of a list of numbers"""
    mean = calculate_mean(lst)
    variance = sum((x - mean)**2 for x in lst) / len(lst)
    return variance

# Standard Deviation
def calculate_std(lst):
    """Calculate the standard deviation of a list of numbers"""
    variance = calculate_variance(lst)
    std = variance ** 0.5
    return std 