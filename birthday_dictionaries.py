birthday_dictionaries = {"Thiago": "08/10/1990" , "Patricia" : "21/09/1992" , "Rodrigo" : "02/02/1987" , "Anne" : "20/08/1988" , "Rafael" : "06/12/1989" , "Allan" : "07/05/1989" }

def welcome_messages(dict):
    known_births = []
    for key,value in dict.items():
        known_births.append(key)

    print("We know the birthdays of \n{}".format("\n".join(known_births)))

    answer = input("Please type the name from who you wish to know the birthday!!!\n")

    for key,value in dict.items():
        if key == answer:
            print(value)



welcome_messages(birthday_dictionaries)



