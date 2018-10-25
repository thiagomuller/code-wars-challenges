#Need to correct this one, the characters must be sorted in order of appearance, instead of alphabetic order


def ordered_count(arr):
    arr_dict = {}
    arr_ltr_dict = {}
    arr_list = []

    arr_ltr_list = [ltr for ltr in arr]

    for var in arr:
        arr_dict[var] = arr.count(var)

    counter = 0
    for ltr in arr_ltr_list:
        arr_ltr_dict[ltr] = counter
        counter += 1

    #return arr_list
    print("arr_dict: {}".format(arr_dict))
    print("arr_ltr_dict: {}".format(arr_ltr_dict))
    print("arr_ltr_list: {}".format(arr_ltr_list))

arr = "abracadabra"
ordered_count(arr)