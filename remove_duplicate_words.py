#This is a exercise in which we're given a string containing repeated words, in which we must find those repeated words and remove then, returning a string that doesn't contain any repeated words




#The logic here is to split the given string into a list, each word an element of the list, then iterate over it,  compairing to an empty result list, then, every time the word isn't on result list,
# we append it to it. After that, we use .join string concatenation method to turn result list back into a string, then we return it
def remove_duplicate_words(s):
    result_list = []
    word_list = s.split()


    for var in word_list:
        if var not in result_list:
            result_list.append(var)


    return " ".join(result_list)   #this .join method is called upon a string, which it uses as a separator between the values of the list it received as parameter, very cool feature










string  = "my cat cat is fat fat"
print(remove_duplicate_words(string))
