def imp_range(*args):

    if len(args) == 1:
        stop = args[0]
        start = 0
        step = 1

        result_list = []

        while start <= stop - 1:
                result_list.append(start)
                start = start + step

        return result_list

    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1

        result_list = []

        lock = start

        while start <= stop - 1:
            if step == 0:
                result_list.append(lock)
                start += 1
            elif step > 0:
                result_list.append(start)
                start = start + step

        return result_list

    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]

        result_list = []

        lock = start

        while start <= stop - 1:
            if step == 0:
                result_list.append(lock)
                start += 1
            elif step > 0:
                result_list.append(start)
                start = start + step

        return result_list


print(imp_range(0,30))
