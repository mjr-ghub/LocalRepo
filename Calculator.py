num1 = float(input("Enter 1st number:- "))
num2 = float(input("Enter 2nd number:- "))

operator = input("Enter the operation(+ - * /):- ")

if operator == "+":
    result= num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
        result= num1 * num2
        print(result)
elif operator == "/":
        result= num1 / num2
        print(result)
else:
      print("{operator} is not a valid option")