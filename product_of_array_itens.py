def product(numbers):
    result = []
    for var in range(0,len(numbers)):
        result = numbers[var] * numbers[var-1]
    print(result)


numbers = [5,4,1,3,9]
product(numbers)