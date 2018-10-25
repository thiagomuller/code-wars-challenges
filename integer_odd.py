def find_it(seq):
        repeated = {}
        for var in seq:
                if var not in repeated:
                    repeated[var] = 1
                else:
                    repeated[var] += 1
        print(repeated)

        for key,value in repeated.items():
            if value > 1 and value %2 == 1:
                return key

arr = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(arr))