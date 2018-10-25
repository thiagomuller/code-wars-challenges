#this is a code to two lists of tuples, each tuple containing two values, that means, a matrix with a n number of lines, but always two columns
# def tuples_list_password(ftup,stup):
#
#     result_list = []
#     result = ""
#
#     for fvlr, svlr in zip(ftup, stup):
#         if fvlr[0] == svlr[0]:
#             result_list.append(fvlr[0])
#         elif fvlr[0] == svlr[1]:
#             result_list.append(fvlr[0])
#         elif fvlr[1] == svlr[0]:
#             result_list.append(svlr[0])
#         elif fvlr[1] == svlr[1]:
#             result_list.append(svlr[1])
#
#     for var in result_list:
#         result += str(var)
#
#     print(result)


#now, if I mean to expand this code to accept n number of lines and n number of columns, how can I do so?


def tuples_list_password(*args):

    input_list = []
    for var in args:
        input_list.append(var)

    final_list = []
    for num in range(len(input_list)):
        if num > 0 and num < len(input_list):
            for fvlr,svlr in zip(input_list[num - 1] , input_list[num]):
                for a in fvlr:
                    for b in svlr:
                        if a == b:
                            if a not in final_list:
                                final_list.append(a)


    return final_list



tup1 = [(9,4,3) , (5,7,8,2) , (4,3,2,1)]
tup2 = [(4,7,6,1,2) , (6,9,4,7) , (1,8)]
tup3 = [(8,5,12,45,98,4), (45,22,34,10,7) , (188,34,20,1,40)]
tup4 = [(44,35,68,4,23,108,256) , (7,455,28,19,23,100,103) , (109,1,204,306,80)]

arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
arr3 = [11,12,13,14,15]
arr4 = [16,17,18,19,20]

print(tuples_list_password(tup1,tup2,tup3,tup4))
