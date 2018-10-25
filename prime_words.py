def prime_number(num):
    prime_counter = 0
    for var in range(1,num+1):
        if(num % var == 0 or num % var == num):
            prime_counter += 1
    return (prime_counter == 2)



def prime_word(array):

    result_list = []

    for var in array:

        counter = 0


        for wrd in var[0]:
            if prime_number(ord(wrd) + var[1]):
                counter += 1


        if counter >= 1:
            result_list.append(1)
        else:
            result_list.append(0)

    return result_list


array = [["Emma",45],["Liam",30]]
prime_word(array)


