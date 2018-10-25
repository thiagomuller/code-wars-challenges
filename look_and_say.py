def look_and_say(arr):

    result_list = []
    arr = []


    for var in array:
        arr.append(var)

    counter = 0
    for num in range(0,len(arr) - 1):
        if num > 0 and arr[num] == arr[num - 1]:
            counter += 1
            print("num: {} , arr[num]: {}, arr[num-1]: {}, counter: {}".format(num, arr[num], arr[num - 1], counter))
        elif num > 0 and arr[num] != arr[num - 1]:
            # print(counter + 1, num - 1 , num)
            #print(counter)
            result_list.append(counter + 1)
            counter = 0
        #print(counter)

        result_list.append(arr[num - 1])


    return result_list







array = "11223"
print(look_and_say(array))