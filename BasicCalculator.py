print("---------BASIC CALCULATOR--------")

num1 = input("num1: ")
operation = input("choose(+-*/): ")
num2 = input("num2: ")
num1 = float(num1)
num2 = float(num2)
if(operation.__eq__("+")):
    result = num1+num2
elif(operation.__eq__("-")):
    result = num1-num2
elif(operation.__eq__("*")):
    result = num1*num2
elif(operation.__eq__("/")):
    result = num1/num2
else:
  result = "invalid input"
print(result)

