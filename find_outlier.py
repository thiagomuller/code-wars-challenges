#This is a exercise in which I receive an array containing either all its integers as even except for one, or all its integers odds expect for one.
#My task here is to find the only one different

#The logic here is to generate two lists using list comprehension, one for evens, other for odds, each lists will contain only the odds or evens from the original integers list
#After that we compare both of the lists two see which of them have the lower size, and then return the first (and unique) element of that list

def find_outlier(integers):
    evens = [a for a in integers if a % 2 == 0]   #Generating a list containing only the evens from the original integers list
    odds = [a for a in integers if a % 2 == 1]    # Generating a list containing only the odds from the original integers list

    return evens[0] if len(evens) < len(odds) else odds[0]   #Return first and only element from evens if its size is lower than odds, and vice versa


integers = [19 , 35, 4, 13, 23, 3]

print(find_outlier(integers))

