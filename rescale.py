def rescale_list(original_list):
    max_val = max(original_list)
    min_val = min(original_list)
    rescaled_list = []
    for val in original_list:
        rescaled_val = 1 + (val - min_val) * 4 / (max_val - min_val)
        rescaled_list.append(rescaled_val)
    return rescaled_list
