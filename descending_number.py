def Descending_Order(num):
    str_number_list = sorted([a for a in str(num)] , reverse=True)
    str_number = ""
    for var in str_number_list:
        str_number += var

    number = int(str_number)
    return number









number = 21445
print(Descending_Order(number))