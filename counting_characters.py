def ordered_count(input):
    input_list = [a for a in input]
    ch_counter = {}
    for key in input_list:
            if key not in ch_counter:
                ch_counter[key] = 1
            else:
                ch_counter[key] += 1











first_word = "abracadabra"
print(ordered_count(first_word))