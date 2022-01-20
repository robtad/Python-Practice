from curses.ascii import isalnum, isalpha

print("------------BASIC CALCULATOR-----------")
print("-----------Press 'e' to exit!----------")
print("---------Enter Math Expression---------")

def Calculator(operation):
    if isalpha(operation[0]) or not(isalnum(operation[0])):
      print("Invalid Input")
      return
    for i in range(0, len(operation)):
        if(operation[i] == "+" or operation[i] == "-" or operation[i] == "*" or operation[i] == "/"):
            operator = operation[i]
            index = i
            break
        else:
            continue
        i += 1
    a = ""
    b = ""
    if(index != 0 and index != len(operation)-1):
        for x in range(0, index):  # increments 1 by default no need to add third parameter
            a += operation[x]
        for x in range(index+1, len(operation)):
            b += operation[x]

        a = float(a)
        b = float(b)
        if(operator.__eq__("+")):
            print( ':', a+b)
        elif(operator.__eq__("-")):
            print( ':', a-b)
        elif(operator.__eq__("*")):
            print( ':', a*b)
        elif(operator.__eq__("/") and b == 0):
            print('Infinity')
        elif(operator.__eq__("/")):
            print( ':', a/b)
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")

while True:
    mathExp = input()
    if mathExp == "e":
        break
    Calculator(mathExp)
