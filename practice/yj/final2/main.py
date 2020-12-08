from Cal import Cal
cal = Cal()
cal.operand1 = float(input())
expression = input()
cal.operand2 = float(input())

print(cal.calculate("__"+expression))
