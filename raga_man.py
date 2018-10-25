def a_raga_man(fstring , sstring):

    first_string = fstring.lower().strip()
    second_string = sstring.lower().strip()


    counter = 0
    if len(first_string) == len(second_string):
        for var in fstring:
            for ltr in sstring:
                if var == ltr:
                    counter += 1

        if counter == len(fstring):
            return True
        else:
            return False

    else:
        return False

