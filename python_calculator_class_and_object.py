# basic calculator

class Calculator:

    def __init__(self,operand1,operand2):

        self.operand1=operand1

        self.operand2=operand2

    def addition_of_two_numbers(self):

        result= self.operand1  + self.operand2

        print(result)

    def substraction_of_two_numbers(self):

        result= self.operand1 - self.operand2

        print(result)

    def multiplication_of_two_numbers(self):

        result= self.operand1 * self.operand2

        print(result)

    def division_of_two_numbers(self):

        result = self.operand1 / self.operand2

        print(result)

    def exponential_of_two_numbers(self):

        result = self.operand1 ** self.operand2

        print(result)

d = Calculator(5,8)
d.addition_of_two_numbers()
d.substraction_of_two_numbers()
d.multiplication_of_two_numbers()
d.division_of_two_numbers()
d.exponential_of_two_numbers()
    




