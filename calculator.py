print("let's do some arithmetic. Pick two numbers and an operation to continue.")
number1 = int(input("pick the firstnumber : "))
number2 = int(input("Pick the second number : "))
print()
print("What operation would you like to perform?")
print("Type + for addition")
print("Type - for substraction")
print("type / for division")
print("type * for multiplication")
operation = input("operation of choice : ")

print()
if operation == "+":
    result = (number1 + number2)
    print("The result of your request is : ")
    print(result)
elif operation == "-":
    result = (number1 - number2)
    print("The result of your request is : ")
    print(result)
elif operation == "/":
    result = (number1 / number2)
    print("The result of your request is : ")
    print(result)
elif operation == "*":
    result = (number1 * number2)
    print("The result of your request is : ")
    print(result)
else :
    print("I don't recognise that operation.")