class Cal:
    def __init__(self):
        self.operand1 = None
        self.operand2 = None
    def __add(self, operand1, operand2):
        return (operand1+operand2)
    def __sub(self, operand1, operand2):
        return (operand1-operand2)
    def __mul(self, operand1, operand2):
        return (operand1*operand2)
    def __div(self, operand1, operand2):
        return (operand1/operand2)
    def __rem(self, operand1, operand2):
        return (operand1%operand2)

#     def calculate(self, expression):
#         if expression == 'add':
#             print(self.__add(self.operand1, self.operand2))
#         elif expression == 'sub':
#             print(self.__sub(self.operand1, self.operand2))
#         elif expression == 'mul':
#             print(self.__mul(self.operand1, self.operand2))
#         elif expression == 'div':
#             print(self.__div(self.operand1, self.operand2))
#         elif expression == 'rem':
#             print(self.__rem(self.operand1, self.operand2))
#         else:
#             print("해당 계산기능은 없습니다.")
#
#
# cal = Cal()
# cal.operand1 = float(input())
# expression = input()
# cal.operand2 = float(input())
# cal.calculate(expression)

    def calculate(self, expression):
        if expression == 'add' or  expression =='+':
            return self.__add(self.operand1, self.operand2)
        elif expression == 'sub'or expression =='-':
            return self.__sub(self.operand1, self.operand2)
        elif expression == 'mul'or expression =='*':
            return self.__mul(self.operand1, self.operand2)
        elif expression == 'div'or expression =='/':
            return self.__div(self.operand1, self.operand2)
        elif expression == 'rem' or expression =='%':
            return self.__rem(self.operand1, self.operand2)
        else:
            print("해당 계산기능은 없습니다.")


cal = Cal()
# cal.operand1 = float(input())
expression = input()
# cal.operand2 = float(input())
cal.operand1, cal.operand2 = map(float, input().split())
print(cal.calculate(expression))
