import math


class Calculator_POO:

    def __init__(self, number_1=0, number_2=0):
        self._number_1 = number_1
        self._number_2 = number_2

    @property
    def number_1(self):
        return self._number_1
    @number_1.setter
    def number_1(self , value):
        self._number_1 = value
        return self._number_1

    @property
    def number_2(self):
        return self._number_2

    @number_2.setter
    def number_2(self, value):
        self._number_2 = value
        return self._number_2


    def sum_numbers(self , a , b):
        print(a + b , end="\n")

    def sub_numbers(self , a , b):
        print(a - b , end="\n")

    def div_numbers(self , a , b):
        print(a / b , end="\n")

    def mult_numbers(self , a , b):
        print(a * b , end="\n")

    def sin_number(self , a):
        print(math.sin(a))

    def cos_number(self , a):
        print(math.cos(a))

    def welcome_messages(self):
        print("Welcome to CalculatorPOO\n")
        self._number_1 = int(input("Please type your first number\n"))
        self._number_2 = int(input("Please type your second number\n"))

    def which_operation(self):
        print("Which operation would you like to choose?\n")
        print("1 - Sum\n")
        print("2 - Sub\n")
        print("3 - Div\n")
        print("4 - Mult\n")
        print("5 - Sin(x)\n")
        print("6 - Cos(x)\n")
        operation = int(input().strip().lower())
        if(operation == 1):
            self.sum_numbers(self._number_1 , self._number_2)
        elif (operation == 2):
            self.sub_numbers(self._number_1, self._number_2)
        elif (operation == 3):
            self.div_numbers(self._number_1, self._number_2)
        elif (operation == 4):
            self.mult_numbers(self._number_1, self._number_2)
        elif (operation == 5 or operation==6):
            term = input("From which term, first or second number?\n")
            self.which_term(term , operation)

    def which_term(self , term , operation):
        if (term == "first"):
            if(operation == 5):
                self.sin_number(self.number_1)
            elif(operation == 6):
                self.cos_number(self.number_1)
        elif(term == "second"):
            if (operation == 5):
                self.sin_number(self.number_2)
            elif (operation == 6):
                self.cos_number(self.number_2)

inst1 = Calculator_POO()
inst1.welcome_messages()
inst1.which_operation()

