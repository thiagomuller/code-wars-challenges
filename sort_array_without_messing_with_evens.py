def sort_array(arr):
    odds_only = sorted([a for a in arr if a % 2 == 1])
    enumerated_arr = [a for a in enumerate(arr)]
    sorted_list = []
    for key,var in enumerated_arr:
            if var % 2 == 0:
                sorted_list[key] = var
            else:
                sorted_list[key] = odds_only[key]
    return sorted_list







arr = [5, 3, 2, 8, 1, 4]
print(sort_array(arr))