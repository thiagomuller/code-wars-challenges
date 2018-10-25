#Just creating my own version of python map function, just to understand its work



def square_value(value): #creating a function to be used as parameter to my mapping function in this case
    return value**2


def mapping_myself(func,iter): #creating the mapping function itself, that receives a function and a iterable
    result_list = []
    for num in range(len(iter)):
        result_list.append(func(iter[num]))
    return result_list




arr = [2,4,3,2]
print(mapping_myself(square_value,arr))